from flask import Blueprint, render_template

ash_bp = Blueprint("ASH Blueprint",__name__,url_prefix='/ash',template_folder='templates')

@ash_bp.route("/")
def ash_index():
    return render_template("ash/naked.html")

