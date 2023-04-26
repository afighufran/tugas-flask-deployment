from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)


@app.route("/")
def home():
    return "Belajar Flask Dasar"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
