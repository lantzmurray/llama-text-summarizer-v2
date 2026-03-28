"""Streamlit Frontend - Text Summarizer (Project 1)"""

import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Text Summarizer - School of AI Project 1",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("LLaMA Text Summarizer")
st.markdown("Summarize text using LLaMA 2 model via Ollama")

# Input section
st.header("Input")

text_input = st.text_area("Enter your text here:", height=200)

# Process button
if st.button("Summarize"):
    with st.spinner("Processing..."):
        try:
            response = requests.post(
                "http://localhost:8000/summarize/",
                data={"text": text_input}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Display result
                st.success("Done!")
                st.subheader("Summary:")
                st.write(result.get("summary", "Error generating summary."))
            else:
                st.error(f"Error: {response.status_code}")
                
        except Exception as e:
            st.error(f"Connection error: {str(e)}")



# Footer
st.markdown("---")
st.markdown("*Part of School of AI 10-week internship program*")
