# Ollama Chatbot

A simple command-line chatbot powered by [Ollama](https://ollama.com), using the `gemma4:e4b` model.

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com/download) installed and running locally
- The `gemma4:e4b` model pulled in Ollama
- `ollama` Python package

## Setup

1. Install Ollama and make sure the Ollama service is running.

2. Pull the model:

   ```
   ollama pull gemma4:e4b
   ```

3. Install the Python dependency:

   ```
   pip install ollama
   ```

## Usage

Run the chatbot:

```
python agent.py
```

Enter a prompt at the `Enter your prompt:` input. Type `quit` to exit.

## Version
1.0 - basic chatbot that uses ollama:gemma4 (no memory)
