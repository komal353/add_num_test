# FastAPI Add Numbers Application

A simple FastAPI application that adds two numbers together. This project demonstrates basic FastAPI functionality with request/response validation using Pydantic models.

## Features

- ✨ Add two numbers via POST request with JSON payload
- 📍 Add two numbers via GET request with URL path parameters
- 📚 Interactive API documentation (Swagger UI)
- ✅ Input validation using Pydantic models
- 📝 Fully documented endpoints

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server using one of these methods:

**Option 1: Using Python directly**
```bash
python main.py
```

**Option 2: Using Uvicorn**
```bash
uvicorn main:app --reload
```

The application will start on `http://localhost:8000`

## API Endpoints

### Root Endpoint
- **URL**: `GET /`
- **Description**: Welcome message and API info
- **Response**: 
```json
{
  "message": "Welcome to Add Numbers API",
  "version": "1.0.0"
}
```

### Add Numbers (POST)
- **URL**: `POST /add`
- **Description**: Add two numbers using JSON payload
- **Request Body**:
```json
{
  "num1": 10,
  "num2": 20
}
```
- **Response**:
```json
{
  "num1": 10,
  "num2": 20,
  "sum": 30
}
```

### Add Numbers (GET)
- **URL**: `GET /add/{num1}/{num2}`
- **Description**: Add two numbers using URL parameters
- **Example**: `GET /add/15/25`
- **Response**:
```json
{
  "num1": 15,
  "num2": 25,
  "sum": 40
}
```

## Interactive Documentation

After starting the server, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Testing

You can test the API using curl or any API client:

**POST example:**
```bash
curl -X POST "http://localhost:8000/add" \
  -H "Content-Type: application/json" \
  -d '{"num1": 5, "num2": 10}'
```

**GET example:**
```bash
curl "http://localhost:8000/add/5/10"
```

## Project Structure

```
.
├── main.py           # FastAPI application
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Technologies Used

- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI web server
- **Pydantic**: Data validation using Python type annotations
