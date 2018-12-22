from flask import Flask, render_template, request, jsonify
from datetime import datetime
import psycopg2
import os

app = Flask(__name__)
app.secret_key = "shinedownisalittlebad"

db = os.environ['DATABASE_URL']
conn = psycopg2.connect(db)
print(conn, 11)
print(conn.cursor())

current_id = None


def get_last_row(cursor):
    print("GETTING LAST ROW")
    sql = "SELECT MAX(id) FROM letters"
    cursor.execute(sql)
    value = cursor.fetchone()[0]
    print(value, 22)
    if not value:
        print("NOT VALUE")
        sql = "INSERT INTO letters DEFAULT VALUES"
        cursor.execute(sql)
        conn.commit()
        print("INSERtED INTO DB")
        sql = "SELECT MAX(id) FROM letters"
        cursor.execute(sql)
        value = cursor.fetchone()[0]
    print(value, 28)
    return value


def add_new_row(cursor):
    sql = "INSERT INTO letters DEFAULT VALUES"
    cursor.execute(sql)
    conn.commit()
    global current_id
    current_id = cursor.lastrowid


def get_letter_string(cursor):
    print("GETTING LETTER STRING", 41)
    sql = "SELECT string FROM strings WHERE DATE(datetime) = CURRENT_DATE"
    cursor.execute(sql)
    value = cursor.fetchone()[0]

    print(value, 46)

    return value


def add_letter_to_db(letter, cursor):
    value = get_letter_string(cursor)

    if not value:
        sql = "INSERT INTO strings DEFAULT VALUES"
        cursor.execute(sql)
        conn.commit()

        value = ""

    sql = "UPDATE strings SET string = CONCAT(string, %s) WHERE DATE(datetime) = CURRENT_DATE"
    cursor.execute(sql, [letter])
    conn.commit()

    return value + letter


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update_letter", methods=["POST"])
def update_letter():
    cursor = conn.cursor()

    global current_id
    current_id = get_last_row(cursor)

    letter = request.form["letter"]
    sql = "SELECT " + letter + " FROM letters WHERE id = %s"
    cursor.execute(sql, [current_id])
    value = cursor.fetchone()[0]

    sql = "UPDATE letters SET " + letter + " = %s WHERE id = %s"
    val = (value + 1, current_id)
    cursor.execute(sql, [val])
    conn.commit()

    cursor.close()

    return "success"


@app.route("/get_time", methods=["GET"])
def get_time():
    now = datetime.now()
    return jsonify(now.strftime("%S"))


@app.route("/get_chosen_letter", methods=["GET"])
def get_chosen_letter():
    print("GETTING CHOSEN LETTER")
    cursor = conn.cursor()

    global current_id
    current_id = get_last_row(cursor)
    print(current_id, 108)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sql = "SELECT a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z FROM letters WHERE id = '%s'"
    cursor.execute(sql, [current_id])
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

    add_new_row(cursor)
    letter_string = add_letter_to_db(result, cursor)
    print(letter_string, 123)

    cursor.close()

    return jsonify(letter_string)


@app.route("/get_current_string")
def get_current_string():
    cursor = conn.cursor()
    print(cursor, 133)

    letter_string = get_letter_string(cursor)

    cursor.close()
    return jsonify(letter_string)