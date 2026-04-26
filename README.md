# Project 1: LLaMA Text Summarizer

A local AI text summarization application that uses LLaMA 2 via Ollama to generate concise summaries of long text documents. Perfect for content creators, students, researchers, and anyone who needs to quickly understand lengthy documents.

## Features

- **Text Summarization**: Generates concise summaries of long documents
- **Key Points Extraction**: Identifies main themes and important information
- **Bullet Point Format**: Organizes summary into digestible points
- **FastAPI Backend**: Efficient REST API for text processing
- **Streamlit Frontend**: User-friendly interface for text input
- **Local Processing**: All analysis runs locally using Ollama LLMs - no external API dependencies

## Architecture

### Backend Components

1. **Text Summarizer** (`backend/main.py`)
   - Processes text documents
   - Generates concise summaries
   - Extracts key points and themes

2. **API Endpoints** (`backend/main.py`)
   - `/summarize/` - Main summarization endpoint

### Frontend Components

1. **Streamlit UI** (`frontend/app.py`)
   - User interface for text input
   - Results display and visualization
   - Export functionality

2. **Reusable Components** (`frontend/components.py`)
   - Modular UI elements
   - Consistent styling and layout

## Installation

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running (for local LLM inference)

### Setup Steps

1. **Navigate to the project directory**:
   ```bash
   cd SchoolOfAI/Official/soai-01-text-summarizer
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and start Ollama** (if not already installed):
   ```bash
   # Install Ollama from https://ollama.com
   # Pull a model (llama2 is recommended)
   ollama pull llama2
   # Start Ollama service
   ollama serve
   ```

## Running the Application

### Backend API

1. **Start the FastAPI backend**:
   ```bash
   uvicorn backend.main:app --reload
   ```

2. **Access the API**: Navigate to `http://localhost:8000` for API documentation

### Frontend UI

1. **Start the Streamlit application** (in a new terminal):
   ```bash
   streamlit run frontend/app.py
   ```

2. **Open your browser**: Navigate to `http://localhost:8501`

## Usage

### 1. Input Text

- Paste long text in the text area
- Or upload a text file
- Sample data provided in `Data/sample_text.txt`

### 2. Summarize Text

- Click "Summarize" to process the text
- Wait for the AI to generate a summary
- View the concise overview

### 3. Review Results

- **Summary**: One-paragraph overview of the document
- **Key Points**: Bullet-point format of main themes
- **Word Count**: Statistics on text length and summary

### 4. Export Results

- Copy summary for use in other documents
- Export as text or JSON
- Save for future reference

## Workflow

```
Input Text → Backend API → Ollama LLM → Generate Summary → Display Results
     ↓               ↓            ↓                ↓                  ↓
  Paste text     FastAPI      Call model      Extract key      Show to
  or file        endpoint     with prompt   points        user
```

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root:

```env
OLLAMA_MODEL=llama2
OLLAMA_API_URL=http://localhost:11434/api/generate
```

### Ollama Models

The system supports any Ollama model. Recommended models:
- `llama2` - Good balance of speed and accuracy for summarization (default)

## Project Structure

```
soai-01-text-summarizer/
├── backend/
│   └── main.py                  # FastAPI backend
├── frontend/
│   ├── app.py                    # Streamlit UI
│   └── components.py             # Reusable UI components
├── Data/
│   └── sample_text.txt         # Sample text for testing
├── requirements.txt              # Python dependencies
└── README.md                   # This file
```

## Dependencies

- `fastapi` - Web API framework
- `uvicorn` - ASGI server
- `streamlit` - Web UI framework
- `requests` - HTTP client for Ollama API
- `python-dateutil` - Date/time parsing

## Troubleshooting

### Ollama Connection Issues

If you see connection errors:
1. Verify Ollama is running: `ollama list`
2. Check the API URL: `curl http://localhost:11434/api/generate`
3. Ensure the model is pulled: `ollama pull llama2`

### Backend API Issues

If the backend isn't responding:
1. Verify uvicorn is running: `ps aux | grep uvicorn`
2. Check the port isn't in use: `lsof -i :8000`
3. Review backend logs for errors

### Frontend Connection Issues

If the frontend can't connect to the backend:
1. Verify both services are running
2. Check the API URL in frontend/app.py
3. Ensure CORS is configured correctly

### Summarization Issues

If summaries aren't being generated:
1. Check that the text is properly formatted
2. Verify the LLM model is appropriate
3. Review the prompts in backend/main.py
4. Try with a different model

### Slow Performance

For faster summarization:
1. Use a smaller model if speed is critical
2. Reduce text length if possible
3. Increase Ollama's GPU resources if available
4. Process text in smaller chunks

## Use Cases

- **Content Creation**: Generate summaries for articles and blog posts
- **Document Review**: Quickly understand long documents
- **Study Aid**: Extract key points for exam preparation
- **Research**: Summarize academic papers
- **Meeting Notes**: Create concise overviews of discussions
- **Report Writing**: Generate executive summaries for presentations

## Important Notes

- All processing happens locally - no data is sent to external servers
- Summary quality depends on the clarity and structure of the input text
- LLaMA 2 is optimized for text summarization tasks
- Summaries are AI-generated and should be reviewed for accuracy
- This tool provides summaries but not a replacement for human understanding

## License

This project is part of the School of AI curriculum.
