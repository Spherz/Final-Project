from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Test", age=321)


# @views.route("/profile/<username>")
# @views.route("/profile")
# def profile():
#     args = request.args
#     name = args.get('name')
#     return render_template("profile.html")
@views.route("/profile")
def profile():
    return render_template("profile.html")


@views.route("/first-module")
def first_module():
    return render_template("firstmodule.html")


@views.route("/second-module")
def second_module():
    return render_template("secondmodule.html")


@views.route("/third-module")
def third_module():
    return render_template("thirdmodule.html")


@views.route("/json")
def get_json():
    return jsonify({'name': 'timmy', 'kakaya-to wlyapa': 10})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("go-to-home")
def got_to_home():
    return redirect(url_for("views.home"))

