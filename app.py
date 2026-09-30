from flask import Flask, render_template, request, redirect
import sqlite3
import subprocess

app = Flask(__name__)


# ---------------- DATABASE ----------------

def init_db():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            maths REAL NOT NULL,
            science REAL NOT NULL,
            english REAL NOT NULL,
            computer REAL NOT NULL,
            total REAL NOT NULL,
            percentage REAL NOT NULL,
            result TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():

    return render_template("index.html")


# ---------------- ADD RESULT ----------------

@app.route("/add", methods=["GET", "POST"])
def add_result():

    if request.method == "POST":

        roll_no = request.form["roll_no"]
        name = request.form["name"]

        maths = float(request.form["maths"])
        science = float(request.form["science"])
        english = float(request.form["english"])
        computer = float(request.form["computer"])

        # Run Java program
        java_result = subprocess.check_output(
            [
                "java",
                "ResultCalculator",
                str(maths),
                str(science),
                str(english),
                str(computer)
            ],
            text=True
        ).strip()

        total, percentage, result = java_result.split("|")

        # Save to database
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO students
                (
                    roll_no,
                    name,
                    maths,
                    science,
                    english,
                    computer,
                    total,
                    percentage,
                    result
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                roll_no,
                name,
                maths,
                science,
                english,
                computer,
                float(total),
                float(percentage),
                result
            ))

            conn.commit()

        except sqlite3.IntegrityError:

            conn.close()

            return """
            <h2>Roll number already exists!</h2>
            <a href="/add">Go Back</a>
            """

        conn.close()

        return redirect("/")

    return render_template("addresult.html")


# ---------------- SEARCH RESULT ----------------

@app.route("/result", methods=["POST"])
def result():

    roll_no = request.form["roll_no"]

    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    conn.close()

    if student:

        return render_template(
            "result.html",
            student=student
        )

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Result Not Found</title>
    </head>

    <body>

        <h2>Student not found!</h2>

        <a href="/">
            Go Back
        </a>

    </body>
    </html>
    """


# ---------------- START APPLICATION ----------------

if __name__ == "__main__":

    init_db()

    app.run(host="0.0.0.0", port=5000)