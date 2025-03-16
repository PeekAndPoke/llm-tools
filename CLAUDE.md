# CLAUDE.md - Guide for Agentic Coding Assistants

## Build & Development

- Setup environment: `python -m venv venv && source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Run server: `python main.py`
- Run tests: `pytest`
- Run single test: `pytest tests/test_file.py::test_function`
- Code linting: `flake8`
- Type checking: `mypy .`

## Code Style Guidelines

- **Imports**: Group imports: stdlib, third-party, local with blank line between groups
- **Formatting**: Follow PEP 8 (4 spaces, 88 max line length)
- **Types**: Use type annotations for all function parameters and return values
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Error Handling**: Use specific exceptions, handle anticipated errors gracefully
- **Documentation**: Docstrings for all modules, classes, and functions
- **Structure**: Use FastMCP framework for tool implementations
- **Tools**: Leverage existing tools from langchain and similar libraries
