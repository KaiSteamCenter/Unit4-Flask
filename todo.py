from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print

connection = pymysql.connect(
    host="10.100.33.60",
    user="mmcfowler",
    password="220878185",
    database="mmcfowler_todos",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
cursor = connection.cursor()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    cursor.execute("SELECT `description` FROM `todos`")
    results = cursor.fetchall()
    print(results)

    if request.method == "POST":
        new_todo = request.form.get("new_todo")
        if new_todo:
            cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")

@app.route("/delete_todo/<int:todo_index>", methods=["POST"])
def todo_delete(todo_index):

    return redirect("/")
