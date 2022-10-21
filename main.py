"""Function to test the fastapi CI/CD Process."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    """This is a test api
    :return: response
    """
    return {"message": "Hello Harish, This is running from app engine"}
