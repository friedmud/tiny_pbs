from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from server.db import get_db

bp = Blueprint('job_manager', __name__)

@bp.route("/qsub")
def qsub():
    return "subbing!"

@bp.route('/qstat')
def login():
    return 'qstat stuff'
