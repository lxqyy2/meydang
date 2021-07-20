from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "这里是首页"


if __name__ == '__main__':
    app.run(debug=True)
