from flask import Blueprint, render_template, request, redirect, url_for, session
from backend.analyzer import analyze_url
from backend.extensions import get_db

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():

    db = get_db()

    total_scans = db.execute(
        "SELECT COUNT(*) FROM scans"
    ).fetchone()[0]

    average_risk = db.execute(
        "SELECT COALESCE(AVG(risk_score), 0) FROM scans"
    ).fetchone()[0]

    threat_distribution = db.execute(
        """
        SELECT threat_level, COUNT(*)
        FROM scans
        WHERE threat_level IN ('SAFE', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')
        GROUP BY threat_level
        """
    ).fetchall()

    recent_scans = db.execute(
        """
        SELECT url, threat_level, risk_score, created_at
        FROM scans
        ORDER BY id DESC
        LIMIT 5
        """
    ).fetchall()


    threats_detected = db.execute(
        """
        SELECT COUNT(*)
        FROM scans
        WHERE threat_level IN ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL')
            AND threat_level != 'INVALID'
        """
    ).fetchone()[0]



    db.close()

    return render_template(
        "dashboard.html",
        total_scans=total_scans,
        average_risk=round(average_risk),
        threat_distribution=threat_distribution,
        recent_scans=recent_scans,
        threats_detected=threats_detected

    )


@main.route("/scanner", methods=["GET", "POST"])
def scanner():

    if request.method == "POST":

        url = request.form.get("url", "")
        result = analyze_url(url)

        db = get_db()

        db.execute(
            """
            INSERT INTO scans (url, threat_level, risk_score, confidence)
            VALUES (?, ?, ?, ?)
            """,
            (
                url,
                result["threat_level"],
                result["risk_score"],
                result["confidence"]
            )
        )

        db.commit()
        db.close()

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

    db = get_db()

    scans = db.execute(
        """
        SELECT id, url, threat_level, risk_score, confidence, created_at
        FROM scans
        ORDER BY id DESC
        """
    ).fetchall()

    db.close()

    return render_template(
        "history.html",
        scans=scans
    )

@main.route("/history/clear", methods=["POST"])
def clear_history():

    db = get_db()

    db.execute("DELETE FROM scans")

    db.commit()
    db.close()

    return redirect(url_for("main.history"))


@main.route("/about")
def about():
    return render_template("about.html")