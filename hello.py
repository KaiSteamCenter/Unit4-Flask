# C:\Users\notpo\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m flask --app hello --debug run
# python -m flask --app hello --debug run
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')


def index():
    user_name = "worldpremieres"
    return render_template("home.html.jinja",username=user_name)



@app.route('/ping')

def ping():
    return "<h1>Pong</h1> \n <h2><a href='/'>Index</a></h2>"


@app.route('/hello/<name>')
def hello(name):
    return f"<h1>Hello {name}</h1>"