import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
API_KEY_BLOG = os.getenv("API_KEY_blog")

app = Flask(__name__)
all_posts = requests.get(f"https://api.npoint.io/{API_KEY_BLOG}").json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)
