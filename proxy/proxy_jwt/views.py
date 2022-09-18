
'''
Blueprint API endpoints.

_AuthManager: AuthManager() instance
uptime: Stores app uptime
'''

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
    '''
    API: HTTP Proxy with JWT injection.
    Request: POST, any JSON payload
    '''
    response, code = _AuthManager.proxy(request = request)
    return jsonify(response), code

# Proxy echo
@blueprint.route('/echo', methods=['POST'])
def echo():
    '''
    API: HTTP request echo.
    Request: POST, any JSON payload
    '''
    response, code = _AuthManager.echo(request = request)
    return jsonify(response), code

# Status page
@blueprint.route('/status', methods=['GET'])
def status():
    '''
    API: service status.
    Request: GET
    '''
    req_count = Requests.query.with_entities(func.count(Requests.id)).scalar()
    return render_template('status.html', uptime = uptime, req_count = req_count)
