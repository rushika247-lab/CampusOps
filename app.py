from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("login.html")


# ---------------- LOGIN ROUTES ----------------
@app.route("/admin-login", methods=["POST"])
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":
        return render_template("admin.html")

    return """
    <h2>Invalid Admin Credentials</h2>
    <a href="/">Back to Login</a>
    """


@app.route("/faculty-login", methods=["POST"])
def faculty_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "faculty" and password == "faculty123":
        return render_template("faculty.html")

    return """
    <h2>Invalid Faculty Credentials</h2>
    <a href="/">Back to Login</a>
    """


@app.route("/student-login", methods=["POST"])
def student_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "student" and password == "student123":
        return render_template("student.html")

    return """
    <h2>Invalid Student Credentials</h2>
    <a href="/">Back to Login</a>
    """


# ---------------- ADMIN PAGES (NEW FIX) ----------------

@app.route("/students")
def students():
    return render_template("students.html")


@app.route("/teachers")
def teachers():
    return render_template("teachers.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/attendance")
def attendance():
    return render_template("attendance.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)