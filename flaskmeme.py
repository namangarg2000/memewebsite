#!/bin/python3
from distutils.log import debug
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    meme_pic, subreddit = getMeme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


def getMeme():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response['subreddit']
    return meme_large,subreddit

app.run(host="0.0.0.0", port=3000)