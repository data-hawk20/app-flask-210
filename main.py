from flask import Flask
# script for heroku launch/ flask app
app = Flask(__name__)

@app.route('/', methods =['GET','POST'])
def index():
    return "<h1>this is flask application created by Me</h1>"

if __name__ == "__main__":
    app.run()
