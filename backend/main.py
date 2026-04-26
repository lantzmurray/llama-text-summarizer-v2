"""
Backend API for Text Summarizer using LLaMA 2 via Ollama.

This FastAPI application provides an endpoint that accepts text input
and returns a summarized version using a locally-hosted LLaMA 2 model.
"""

from fastapi import FastAPI, Form
import requests
import json

app = FastAPI()
OLLAMA_TIMEOUT_SECONDS = 1800
OLLAMA_API_URL = "http://localhost:11434/api/generate"

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    """
    Summarize the provided text using LLaMA 2 via Ollama.

    Args:
        text: The input text to summarize (from HTML form data)

    Returns:
        A dictionary containing the summarized text under the key "summary"
    """
    # Construct the prompt for the LLM - instructing it to summarize
    # The "\n\n" separation helps the model distinguish instruction from content
    prompt = f"Summarize the provided text into no more than 2 paragraphs:\n\n{text}"

    # Create the request payload with streaming enabled
    payload = {
        "model": "llama2",  # Using llama2 model for summarization
        "prompt": prompt,   # The formatted prompt with text to summarize
        "stream": True      # Enable streaming for faster responses
    }

    try:
        # Send the POST request to Ollama with streaming enabled
        # json=payload automatically converts the dict to JSON and sets headers
        # timeout=(10, 1800) sets two timeouts:
        #   - 10 seconds to establish the connection
        #   - 1800 seconds (30 minutes) to wait for the response
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=(10, OLLAMA_TIMEOUT_SECONDS), stream=True)
        
        # Check if the request was successful (HTTP status code 200-299)
        response.raise_for_status()  # Raises an exception for 4xx/5xx errors
        
        # When stream=True, Ollama returns multiple JSON objects (one per chunk)
        # We need to accumulate all chunks to get the complete response
        full_response = ""
        for line in response.iter_lines():
            if line:
                # Decode and parse each line as JSON
                chunk_data = json.loads(line.decode('utf-8'))
                # Accumulate the response text from each chunk
                if "response" in chunk_data:
                    full_response += chunk_data["response"]
        
        # Return the complete accumulated response
        return {"summary": full_response.strip()}
        
    except requests.exceptions.ConnectionError:
        # Handle case where Ollama is not running
        return {"summary": "Error: Cannot connect to Ollama. Make sure Ollama is running with 'ollama serve'"}
    except requests.exceptions.Timeout:
        # Handle case where request took too long
        return {"summary": "Error: Request timed out. The model may be processing a very long prompt."}
    except requests.exceptions.RequestException as e:
        # Handle other request-related errors
        return {"summary": f"Error: {str(e)}"}
    except json.JSONDecodeError as e:
        # Handle case where response can't be parsed as JSON
        return {"summary": f"Error: Could not parse API response as JSON - {str(e)}"}
