from flask import render_template, request, url_for, redirect, flash, session
from app.extensions import bcrypt
from app.auth import bp
from app.models.user import user
import app
from werkzeug.security import generate_password_hash, check_password_hash



@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password1']

        user1 = user.query.filter_by(username=username).first()

        if user1 and bcrypt.check_password_hash(user1.password, password):
            session['user_id'] = user1.id
            session['username'] = user1.username
            flash('Вы успешно вошли', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Неправильное имя пользователя или пароль', 'error')

    return render_template('auth/index.html')

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Вы успешно вышли', 'success')
    return redirect(url_for('main.index'))
