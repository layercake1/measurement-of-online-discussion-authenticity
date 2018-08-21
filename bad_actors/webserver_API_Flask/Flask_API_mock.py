from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the index'


if __name__ == '__main__':
    app.run(debug=True)