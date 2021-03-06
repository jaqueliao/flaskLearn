import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        phone = request.form['phone']

        error = None
        if username is None:
            error = '请输入姓名！'
        elif phone is None:
            error = '请输入手机号！'

        if error is None:
            session.clear()
            resp = redirect(url_for('index'))
            resp.set_cookie('username', username)
            resp.set_cookie('phone', phone)
            return resp

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    username = request.cookies.get('username')
    g.username = username
    phone = request.cookies.get('phone')
    g.phone = phone


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.username is None or g.phone is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view