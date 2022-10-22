"""Function to test the fastapi CI/CD Process."""

from fastapi import FastAPI

app = FastAPI()


SAMPLE_RESPONSE = (
    "Hello Gurram Harish, This is running from app engine\n "
    "Kamal was able push code to specific branch and "
    "it automatically runs tests & get deployed in app engine \n "
    "All he needs to do is make changes, commit & "
    "push so that the deployment can be taken care "
    "automatically by CI/CD Process :)"
)


@app.get("/")
def home():
    """This is a test api
    :return: response
    """
    return SAMPLE_RESPONSE
