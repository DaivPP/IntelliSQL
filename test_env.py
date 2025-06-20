import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(f"✅ Loaded API Key: {api_key}") # This line will show what's actually loaded

if not api_key:
    print("❌ Error: GOOGLE_API_KEY is not loaded. Please check your .env file.")
else:
    genai.configure(api_key=api_key)

    # Simple test to confirm it works
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Say hello from IntelliSQL!")
    print("🤖 Gemini Response:", response.text)