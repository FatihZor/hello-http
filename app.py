from flask import Flask
from config import DEBUG, HOST, PORT

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
