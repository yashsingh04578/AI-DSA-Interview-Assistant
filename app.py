import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("your-api-key")



genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

st.title("🤖 AI DSA Interview Assistant")

topic = st.text_input(
    "Enter a DSA Topic",
    placeholder="HashMap, Heap, Binary Search..."
)

if topic:
    with st.spinner("Generating answer..."):
        prompt = f"""
        Explain {topic} for coding interviews.

        Include:
        1. Concept
        2. Time Complexity
        3. Space Complexity
        4. Java Code Example
        5. Common Interview Questions
        """

        response = model.generate_content(prompt)

        st.write(response.text)
       