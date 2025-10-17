from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, shashank from ! 🚀 Updated Version v2 from Automated Build"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
