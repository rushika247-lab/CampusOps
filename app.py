from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("login.html")


# ---------------- ADMIN LOGIN ----------------
@app.route("/admin-login", methods=["POST"])
def admin_login():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin123":
        return render_template("admin.html")

    return """
    <h2>Invalid Admin Credentials</h2>
    <a href="/">Back To Login</a>
    """


# ---------------- FACULTY LOGIN ----------------
@app.route("/faculty-login", methods=["POST"])
def faculty_login():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "faculty" and password == "faculty123":
        return render_template("faculty.html")

    return """
    <h2>Invalid Faculty Credentials</h2>
    <a href="/">Back To Login</a>
    """


# ---------------- STUDENT LOGIN ----------------
@app.route("/student-login", methods=["POST"])
def student_login():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "student" and password == "student123":
        return render_template("student.html")

    return """
    <h2>Invalid Student Credentials</h2>
    <a href="/">Back To Login</a>
    """


# ---------------- REGISTER PAGES ----------------
@app.route("/faculty-register")
def faculty_register():
    return render_template("faculty_register.html")


@app.route("/student-register")
def student_register():
    return render_template("student_register.html")


# ---------------- DASHBOARDS ----------------
@app.route("/students")
def students():
    return render_template("students.html")


@app.route("/teachers")
def teachers():
    return "<h1>Teachers Page Coming Soon</h1>"


@app.route("/courses")
def courses():
    return "<h1>Courses Page Coming Soon</h1>"


@app.route("/student")
def student_dashboard():
    return render_template("student_dashboard.html")


@app.route("/faculty")
def faculty():
    return render_template("faculty.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


# ---------------- EXTRA PAGES ----------------
@app.route("/attendance")
def attendance():
    return "<h1>Attendance Page Coming Soon</h1>"


@app.route("/settings")
def settings():
    return "<h1>Settings Page Coming Soon</h1>"


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    return render_template("login.html")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)