<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# FastAPI Add Numbers Project Instructions

This is a FastAPI application for adding two numbers with built-in API documentation.

## Key Technologies
- **Framework**: FastAPI 0.104.1
- **Server**: Uvicorn 0.24.0
- **Validation**: Pydantic 2.5.0

## Project Overview
- Simple, clean codebase with two main endpoints for adding numbers
- Supports both POST (JSON) and GET (URL parameters) methods
- Includes Swagger UI and ReDoc documentation
- Production-ready with proper error handling and type hints

## Common Tasks
- To run the application: `python main.py` or `uvicorn main:app --reload`
- Access API docs at `http://localhost:8000/docs`
- Test endpoints using curl or Postman
