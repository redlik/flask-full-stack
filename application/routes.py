from application import app, db
from flask import render_template, request
from application.models import Users, Course, Enrollment
from application.forms import LoginForm, RegisterForm


@app.route("/")
def index():
    return render_template("index.html", login=True, index = True)


@app.route("/courses")
def courses():
    courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]
    print(courseData[0]["title"])
    return render_template("courses.html", courseData = courseData, courses = True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", login=True, log = True, form = form, title="Login please")


@app.route("/register")
def register():
    return render_template("register.html", login=True, register = True)

@app.route("/enrollment")
def enrollment():
    id = request.args.get('courseID')
    title = request.args.get('title')
    term = request.args.get('term')
    return render_template("enrollment.html",  data = {"id":id, "title": title, "term": term})



@app.route("/user")
def user():
    # Users(user_id=1, first_name="John", last_name="Jones", email="john@jones.com", password="1234abcd").save()
    # Users(user_id=2, first_name="Mary", last_name="Smith", email="mary@smith.com", password="abcd1234").save()
    users = Users.objects.all()
    return render_template("user.html", users=users)
