from flask import Flask

app = Flask(__name__)

@app.route('/', methods =['get','post'])
def index():
    return "<h1>this is flask application created by Me</h1>"

if __name__ == "__main__":
    app.run()
