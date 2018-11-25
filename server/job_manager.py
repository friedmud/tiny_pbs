from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from server.db import get_db

bp = Blueprint('job_manager', __name__)

@bp.route("/qsub", methods=['POST'])
def qsub():
    db = get_db()
    qsub_data = request.get_json()
    db.execute('insert into job (name, command) values (?, ?)', (qsub_data['name'], qsub_data['command']))
    return "OK"

@bp.route('/qstat')
def login():
    return 'qstat stuff'
