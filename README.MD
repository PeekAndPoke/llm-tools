# LLM-TOOLS Server

This project provides tools to LLMs through Model Context Protocol (MCP), implementing a server that aggregates and
exposes various tool functionalities to language models.

## Overview

LLM-TOOLS is designed to be a bridge between language models and external capabilities. The project:

- Uses FastMCP framework for implementing the MCP server
- Aggregates existing tools from libraries like langchain
- Does NOT implement tool functionality from scratch
- Provides a consistent interface for LLMs to access tools

## Current Tools

The server currently implements these tools:

- **Weather forecast**: Get weather information for locations
- **Web search**: Search the web for information on specific queries

## Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Installation

1. Clone the repository
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

Start the server with:

```bash
python main.py
```

By default, the server runs on port 8000. You can specify a different port:

```bash
python main.py --port 9000
```

## Development

### Adding New Tools

To add a new tool:

1. Create a new tool class in `src/tools/`
2. Implement the tool interface using langchain's `BaseTool`
3. Register the tool in `main.py`

### Testing

Run tests with:

```bash
pytest
```

## Architecture

The project uses a simple architecture:

- `main.py`: Entry point that initializes and runs the MCP server
- `src/tools/`: Contains all tool implementations
- Each tool follows the langchain `BaseTool` interface

