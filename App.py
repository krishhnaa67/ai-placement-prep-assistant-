import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(page_title="AI Placement Prep Assistant")

st.title("🚀 AI Placement Prep Assistant")

resume_text = st.text_area(
    "Paste Your Resume Here",
    height=300
)

if st.button("Analyze Resume"):

    if resume_text.strip():

        with st.spinner("Analyzing Resume..."):

            prompt = f"""
            Analyze this resume.

            Give:
            1. Strengths
            2. Weaknesses
            3. Missing Skills
            4. ATS Score out of 100
            5. 10 Interview Questions

            Resume:
            {resume_text}
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.subheader("📊 Analysis Report")
            st.write(response.choices[0].message.content)

    else:
        st.warning("Please paste your resume first.")