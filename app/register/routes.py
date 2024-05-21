from flask import render_template, request, url_for, redirect, flash
from app.extensions import db
from app.extensions import bcrypt
from app.register import bp
from app.forms.forms import RegisterForm, LoginForm
from app.models.user import user
from werkzeug.security import generate_password_hash, check_password_hash



@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if (len(request.form['username']) > 4) and (len(request.form['password1']) > 4) and (
                request.form['password1'] == request.form['password2']):
            hash = bcrypt.generate_password_hash(request.form['password1']).decode('utf-8')
            new_user = user(username=request.form['username'],
                            password=hash,
                            email=request.form['email'])
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('register.index'))
        else:
            flash("Неверно заполнены поля", 'error')
    return render_template("register/index.html")
