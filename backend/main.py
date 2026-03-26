"""FastAPI Backend - Text Summarizer (Project 1)"""

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from shared.backend.llm_client import LLMClient
from shared.backend.error_handling import APIError, api_error_handler, validate_input, log_api_call
import time

app = FastAPI(title="Text Summarizer - School of AI Project 1", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM client with Ollama
llm_client = LLMClient(provider="ollama", model="llama2")

@app.post("/summarize/")
async def summarize(text: str = Form(...)):
    """Summarize text using LLaMA 2"""
    start_time = time.time()
    
    try:
        # Validate input
        validate_input({"text": text})
        
        # Create prompt
        prompt = f"Summarize this text:\n\n{text}"
        
        # Query LLM
        result = llm_client.query(prompt)
        
        execution_time = time.time() - start_time
        
        # Log API call
        log_api_call("/summarize/", "POST", 200, execution_time)
        
        return {"summary": result}
        
    except APIError as e:
        execution_time = time.time() - start_time
        log_api_call("/summarize/", "POST", e.status_code, execution_time)
        raise e
    except Exception as e:
        execution_time = time.time() - start_time
        log_api_call("/summarize/", "POST", 500, execution_time)
        raise APIError(
            status_code=500,
            detail=f"Internal server error: {str(e)}",
            context={"original_error": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
