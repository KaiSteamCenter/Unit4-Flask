from flask import Flask, render_template, request

app = Flask(__name__)

todo = ["Get money", "Get an extra certification"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_todo = request.form.get("new_todo")
        todo.append(new_todo)
    return render_template("todo.html.jinja", todos=todo)
