from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Add Numbers API",
    description="A simple API to add two numbers",
    version="1.0.0"
)


class Numbers(BaseModel):
    """Request model for adding two numbers"""
    num1: float
    num2: float


class AddResult(BaseModel):
    """Response model for the sum result"""
    num1: float
    num2: float
    sum: float


@app.get("/", tags=["Info"])
def read_root():
    """Root endpoint with API information"""
    return {"message": "Welcome to Add Numbers API", "version": "1.0.0"}


@app.post("/add", response_model=AddResult, tags=["Operations"])
def add_numbers(numbers: Numbers):
    """
    Add two numbers together.
    
    - **num1**: First number
    - **num2**: Second number
    
    Returns the sum of the two numbers.
    """
    result = numbers.num1 + numbers.num2
    return AddResult(num1=numbers.num1, num2=numbers.num2, sum=result)


@app.get("/add/{num1}/{num2}", response_model=AddResult, tags=["Operations"])
def add_numbers_query(num1: float, num2: float):
    """
    Add two numbers via URL path parameters.
    
    - **num1**: First number (in URL path)
    - **num2**: Second number (in URL path)
    
    Returns the sum of the two numbers.
    """
    result = num1 + num2
    return AddResult(num1=num1, num2=num2, sum=result)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
