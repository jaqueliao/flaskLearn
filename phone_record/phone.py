import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from phone_record.auth import login_required

bp = Blueprint('phone', __name__)

@bp.route("/")
@login_required
def index():
    return render_template('phone/index.html')


@bp.route("/borrow")
@login_required
def borrow():
    phoneIds = request.form['borrowIds']


@bp.route("/giveBack")
@login_required
def giveBack():
    phoneIds = request.form['giveBackIds']
