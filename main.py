from flask import Flask

app = Flask(__name__)

version = open("app-version.txt", "r")

@app.route("/")
def hello_world():
    return "Hello, welcome to my simple HTTP REST application python-hello version "+version.read()+"."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
