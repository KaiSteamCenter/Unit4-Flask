from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors
from pprint import pprint as print

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "mmcfowler": generate_password_hash("2208781851"),
    "mekhi": generate_password_hash("220878151"),
    "kai": generate_password_hash("220878151"),

}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


connection = pymysql.connect(
    host="10.100.33.60",
    user="mmcfowler",
    password="220878185",
    database="mmcfowler_todos",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


@app.route("/", methods=["GET", "POST"])
@auth.login_required
def index():
    if request.method == "POST":
        new_todo = request.form.get("new_todo")
        if new_todo:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")
            connection.commit()
            cursor.close()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `todos`")
    results = cursor.fetchall()
    print(results)
    cursor.close()
    return render_template("todo.html.jinja", todos=results)


@app.route("/delete_todo/<int:todo_id>", methods=["POST"])
def todo_delete(todo_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = ('{todo_id}')")
    connection.commit()
    cursor.close()
    return redirect("/")


@app.route("/complete_todo/<int:todo_id>", methods=["POST"])
def todo_complete(todo_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT `completion` FROM `todos` WHERE `id` = {todo_id}")
    current_completion = cursor.fetchone()["completion"]
    new_completion = 1 if current_completion == 0 else 0
    cursor.execute(f"UPDATE `todos` SET `completion` = {new_completion} WHERE `id` = {todo_id}")
    connection.commit()
    cursor.close()
    return redirect("/")


if __name__ == "__main__":
    app.run()
