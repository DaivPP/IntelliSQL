import streamlit as st
import sqlite3
import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import GenerativeModel

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = GenerativeModel("gemini-1.5-flash")

# Prompt Instructions
prompt = [
    "You are an expert at converting English questions into SQL queries. The SQL database is named STUDENTS and has the following columns: NAME, CLASS, Marks, Company."
    "\nExample 1: How many entries of records are present?\nSQL: SELECT COUNT(*) FROM STUDENTS;"
    "\nExample 2: Tell me all the students studying in MCom class?\nSQL: SELECT * FROM STUDENTS WHERE CLASS='MCom';"
    "\nOnly return the SQL query without any explanation."
]

# Get SQL query from model response
def get_response(que, prompt):
    response = model.generate_content([prompt[0], que])
    lines = response.text.split("\n")
    for line in lines:
        line = line.strip()
        if line.upper().startswith(("SELECT", "INSERT", "UPDATE", "DELETE")):
            return line
    return "No valid SQL query found."

# Run SQL query
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.commit()
        return rows
    except sqlite3.Error as e:
        return [f"An error occurred: {e}"]
    finally:
        connection.close()

# Home Page
def page_home():
    st.markdown("""
        <style>
            .main-title { color: #00FF00; font-size: 40px; text-align: center; }
            .sub-title { color: #00FF00; font-size: 24px; text-align: center; margin-bottom: 20px; }
            .offerings { color: white; font-size: 18px; padding-left: 20px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-title'>Welcome to IntelliSQL!</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Revolutionizing Database Querying with Advanced LLM Capabilities</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4429/4429822.png", width=200)
    with col2:
        st.markdown("""
            <div class='offerings'>
            <ul>
                <li>Intelligent Query Assistance</li>
                <li>Data Exploration</li>
                <li>Efficient Data Retrieval</li>
                <li>Performance Optimization</li>
                <li>Syntax Suggestions</li>
                <li>Trend Analysis</li>
            </ul>
            </div>
        """, unsafe_allow_html=True)

# About Page
def page_about():
    st.markdown("""
        <style>
            .content { color: white; font-size: 18px; }
            .main-title { color: #00FF00; font-size: 36px; text-align: center; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-title'>About IntelliSQL</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='content'>
            IntelliSQL aims to revolutionize the way users interact with databases by utilizing the power of advanced Large Language Models (LLMs). 
            Our platform offers intuitive and intelligent querying capabilities that simplify SQL interactions for everyone. 
            Whether you're an analyst, developer, or a curious learner, IntelliSQL helps you craft complex queries using simple natural language.
        </div>
    """, unsafe_allow_html=True)
    st.image("https://seeklogo.com/images/O/oracle-sql-developer-logo-848E6FDC1C-seeklogo.com.png", width=150)

# Query Page
def page_intelligent_query_assistance():
    st.markdown("""
        <style>
            .tool-input { margin-bottom: 20px; color: white; }
            .response { color: white; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color: #00FF00;'>Intelligent Query Assistance</h2>", unsafe_allow_html=True)
    st.markdown("IntelliSQL helps users craft complex queries from natural language. It provides suggestions, syntax help, and performance optimization.")

    col1, col2 = st.columns(2)
    with col1:
        with st.form(key="query_form"):
            user_input = st.text_input("Enter your question:")
            submit = st.form_submit_button("Generate SQL Query")

        if submit and user_input:
            try:
                sql_query = get_response(user_input, prompt)
                st.markdown(f"**Generated SQL:** {sql_query}", unsafe_allow_html=True)
                st.text_area("Raw SQL Query", sql_query, height=100)

                results = read_sql_query(sql_query, "students.db")
                st.markdown("### Query Results")
                st.dataframe(results)
            except Exception as e:
                st.error(f"Error: {e}")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3039/3039386.png", width=150)

# Main App Logic
def main():
    st.set_page_config(page_title="IntelliSQL", page_icon="✨", layout="wide")
    st.sidebar.title("Navigation")
    st.markdown("""
        <style>
        .sidebar .sidebar-content { background-color: #2E2E2E; color: white; }
        </style>
    """, unsafe_allow_html=True)

    pages = {
        "Home": page_home,
        "About": page_about,
        "Intelligent Query Assistance": page_intelligent_query_assistance,
    }

    selected = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selected]()

if __name__ == "__main__":
    main()
