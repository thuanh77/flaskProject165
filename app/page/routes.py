from flask import render_template
from app.page import bp


@bp.route('/')
def index():
    return render_template("page/index.html")
