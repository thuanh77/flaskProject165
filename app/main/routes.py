from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.main import bp


@bp.route('/')
def index():
    return render_template("index.html")
