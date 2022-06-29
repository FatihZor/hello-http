from flask import Flask
from config import DEBUG, HOST, MESSAGE, PORT

app = Flask(__name__)

@app.route("/")
def index():
    return MESSAGE

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
