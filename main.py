"""Function to test the fastapi CI/CD Process."""

from fastapi import FastAPI

app = FastAPI()

SAMPLE_RESPONSE = """
<!DOCTYPE html>
<title>Text Example</title>
<style>
  div.container {
    background-color: #ffffff;
  }

  div.container p {
    font-family: Arial;
    font-size: 14px;
    font-style: normal;
    font-weight: normal;
    text-decoration: none;
    text-transform: none;
    color: #000000;
    background-color: #ffffff;
  }
</style>
<div class="container">
  <p>Hello Harish, This is running from app engine</p>
  <p>Kamal was able push code to specific branch</p>
  <p>it automatically runs tests & get deployed in app engine</p>
  <p>All he needs to do is make changes , commit &
  push so that the deployment can be taken care automatically
  by CI/CD Process :)</p>
</div>"""


@app.get("/")
def home():
    """This is a test api
    :return: response
    """
    return SAMPLE_RESPONSE
