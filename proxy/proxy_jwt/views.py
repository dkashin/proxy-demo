
import datetime

from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import func

from proxy.logs import logger_system
from proxy.models import Requests
from proxy.database import db_session

from .auth import AuthManager

_AuthManager = AuthManager(logger = logger_system)

uptime = datetime.datetime.utcnow()

blueprint = Blueprint('proxy_jwt', __name__, template_folder = '../../templates')

# Proxy adding JWT tokens
@blueprint.route('/proxy-jwt', methods=['POST'])
def proxyjwt():
    response, code = _AuthManager.proxy(request = request)
    return jsonify(response), code

# Proxy echo
@blueprint.route('/echo', methods=['POST'])
def echo():
    response, code = _AuthManager.echo(request = request)
    return jsonify(response), code

# Stats page
@blueprint.route('/status', methods=['GET'])
def status():
    req_count = Requests.query.with_entities(func.count(Requests.id)).scalar()
    return render_template('status.html', uptime = uptime, req_count = req_count)
