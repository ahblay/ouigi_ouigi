from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)
app.secret_key = "shinedownisalittlebad"

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'ouigi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ouigi_ouigi'
app.config['MYSQL_DATABASE_DB'] = 'ouigi'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


def get_last_row():
    sql = "SELECT MAX(id) FROM letters"
    cursor.execute(sql)
    value = cursor.fetchone()[0]
    return value


def add_new_row():
    sql = "INSERT INTO letters () VALUES ()"
    cursor.execute(sql)
    conn.commit()
    global current_id
    current_id = cursor.lastrowid
    print(current_id)

current_id = get_last_row()
print(current_id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update_letter", methods=["POST"])
def update_letter():
    letter = request.form["letter"]
    sql = "SELECT " + letter + " FROM letters WHERE id = %s"
    print("TESTING THAT CURRENT ID EXISTS in update_letter")
    print(current_id)
    cursor.execute(sql, current_id)
    value = cursor.fetchone()[0]

    sql = "UPDATE letters SET " + letter + " = %s WHERE id = %s"
    val = (value + 1, current_id)
    cursor.execute(sql, val)
    conn.commit()

    return "success"


@app.route("/get_time", methods=["GET"])
def get_time():
    now = datetime.now()
    return jsonify(now.strftime("%S"))


@app.route("/get_chosen_letter", methods=["GET"])
def get_chosen_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sql = "SELECT a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z FROM letters WHERE id = %s"
    print("TESTING THAT CURRENT ID EXISTS in get_chosen_letter")
    print(current_id)
    cursor.execute(sql, current_id)
    values = cursor.fetchone()
    print(values)
    result = "."
    max = 0
    counter = 0
    for value in values:
        if value > max:
            max = value
            result = alphabet[counter]
        counter += 1

    add_new_row()

    return jsonify(result)