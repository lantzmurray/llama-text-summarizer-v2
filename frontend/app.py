"""
Frontend Application for Text Summarizer.

This Streamlit app provides a user-friendly interface where users can
enter text and receive a summarized version from the LLaMA 2 model
via the FastAPI backend.
"""
# Imports Streamlit and requests modules
import os
import sys

import streamlit as st
import requests

PACKAGE_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from components import render_app_footer, run_with_status_updates

# Set the page title displayed in the browser tab
st.title("LLaMA Text Summarizer")

# Create a text area widget for user input
# The user enters the text they want summarized here
user_input = st.text_area("Enter your text here:")

# Check if the user clicked the "Summarize" button
if st.button("Summarize"):
    # Send the user's text to the backend API for processing
    # Using Form data format to match the backend's Form(...) parameter
    response = run_with_status_updates(
        lambda: requests.post(
            "http://localhost:8000/summarize/",
            data={"text": user_input}
        ),
        start_message="Summarizing your text..."
    )

    # Extract the summary from the JSON response
    # Fallback to error message if key is missing or request fails
    summary = response.json().get("summary", "Error generating summary.")

    # Display the summary section header
    st.subheader("Summary:")

    # Render the summary text on the page
    st.write(summary)


render_app_footer()
