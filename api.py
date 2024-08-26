from flask import Flask

app = Flask(__name__)

@app.route("/my-name")
def hello():
    return "Hi I am First API"

if __name__ == "__main__":
    app.run(debug=True)