# 💡 IntelliSQL – Natural Language to SQL Query Generator

**IntelliSQL** is a user-friendly web application built using **Streamlit** that empowers users to query databases using **natural language**. It uses **Google’s Gemini (1.5 Flash)** model to intelligently convert questions into valid SQL queries and execute them on an SQLite database.

---

## 📌 Features

- 🔍 **Natural Language to SQL** — Ask questions in plain English and get accurate SQL.
- ⚙️ **Integrated Execution** — Runs queries on a preloaded `students.db` database.
- 🧠 **LLM-Powered** — Uses Gemini (Google Generative AI) for intelligent query generation.
- 🎨 **Responsive UI** — Custom dark-themed Streamlit interface.
- 🛡️ **Secure API Handling** — API key stored safely in `.env` file.

---

## 📚 Example Queries

| English Question                                | SQL Generated                                         |
|--------------------------------------------------|--------------------------------------------------------|
| How many entries of records are present?        | `SELECT COUNT(*) FROM STUDENTS;`                      |
| Tell me all the students studying in MCom class?| `SELECT * FROM STUDENTS WHERE CLASS='MCom';`          |
| Who scored more than 80 marks?                  | `SELECT * FROM STUDENTS WHERE Marks > 80;`            |

---

## 🛠️ Tech Stack

- `Python 3.x`
- `Streamlit`
- `Google Generative AI (gemini-1.5-flash)`
- `SQLite`
- `dotenv` for API key management

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DaivPP/IntelliSQL.git
   cd IntelliSQL
