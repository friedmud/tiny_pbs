from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from server.db import get_db

bp = Blueprint('view_jobs', __name__)


@bp.route('/')
def login():
    db = get_db()
    jobs = db.execute('select name, command, submitted, started, finished from job')
    return render_template('view_jobs.html', jobs=jobs)
