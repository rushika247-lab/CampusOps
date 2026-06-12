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


# ---------------- ADMIN MENU PAGES ----------------
@app.route("/students")
def students():
    return render_template("students.html")


# ---------------- STUDENT DASHBOARD ----------------
@app.route("/student")
def student_dashboard():
    return render_template("student_dashboard.html")


# ---------------- FACULTY PAGE ----------------
@app.route("/faculty")
def faculty():
    return render_template("faculty.html")


# ---------------- ADMIN PAGE ----------------
@app.route("/admin")
def admin():
    return render_template("admin.html")


# ---------------- OTHER PAGES ----------------
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


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)