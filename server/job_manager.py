from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from server.db import get_db

bp = Blueprint('job_manager', __name__)

@bp.route("/qsub", methods=['POST'])
def qsub():
    db = get_db()
    qsub_data = request.get_json()
    db.execute('insert into job (name, command) values (?, ?)', (qsub_data['name'], qsub_data['command']))
    db.commit()
    return "OK"

@bp.route('/qstat')
def login():
    db = get_db()
    jobs = db.execute('select name, command, submitted, started, finished from job').fetchall()
    return jsonify([tuple(row) for row in jobs])
