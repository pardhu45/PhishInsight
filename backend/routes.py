from flask import Blueprint, render_template, request, redirect, url_for, session
from backend.analyzer import analyze_url

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():
    return render_template("dashboard.html")


@main.route("/scanner", methods=["GET", "POST"])
def scanner():

    if request.method == "POST":

        url = request.form.get("url", "")
        result = analyze_url(url)

        session["result"] = result

        return redirect(url_for("main.show_result"))

    return render_template(
        "scanner.html",
        result=None,
        url=""
    )
@main.route("/scanner/result")
def show_result():

    result = session.pop("result", None)

    return render_template(
        "scanner.html",
        result=result,
        url=""
    )

@main.route("/analytics")
def analytics():
    return render_template("analytics.html")


@main.route("/history")
def history():
    return render_template("history.html")


@main.route("/about")
def about():
    return render_template("about.html")