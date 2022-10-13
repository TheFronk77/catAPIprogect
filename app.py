from urllib import response
import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def cats():

    url = "https://api.thecatapi.com/v1/images/search?limit=10"
    response = requests.get (url)
    json = response.json()
    url = json[0]["url"]
    
    return "<img src='"+url+"'></img>"

