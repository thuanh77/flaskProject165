from flask import render_template, request, url_for, redirect, flash

from app.extensions import db
from app.auth_user import bp
from app.models.auth_user import Auth_User

from werkzeug.security import generate_password_hash, check_password_hash


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.session.pop('_flashes', None)
        if (len(request.form['username']) > 4 and len(request.form['password']) > 4
                and request.form['password'] == request.form['password2']):
            hash = generate_password_hash(request.form['password'])
            new_user = Auth_User(username=request.form['username'],
                                 password=hash)
            db.session.add(new_user)
            db.session.commit()
            if new_user:
                flash("Вы успешно зарегистрировались!", 'success')
                return redirect(url_for('index'))
            else:
                flash("Ошибка при добавлении в БД", 'error')
        else:
            flash("Неверно заполнены поля", 'error')
    return render_template("auth_user/index.html")
