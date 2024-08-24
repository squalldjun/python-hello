from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, welcome to my simple HTTP REST application!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
