
import datetime, hashlib, jwt, requests, json

from flask import jsonify
from requests.exceptions import RequestException
from sqlalchemy import func

from proxy.models import Requests
from proxy.database import db_session
from proxy.config import app_config


# Auth management class
class AuthManager(object):


    # Class init
    def __init__(self, logger = None):
        self.logger = logger


    # Create JWT token(s)
    def jwt_token(self, user = None):
        utc_time_now = datetime.datetime.utcnow()
        utc_time_now_ts = utc_time_now.timestamp()
        headers = { 'alg': app_config.JWT_ALGORITHM, 'typ': 'JWT' }
        payload = {
            'iat': int(utc_time_now_ts),
            'jti': hashlib.md5(f"{user}{utc_time_now_ts}".encode('utf-8')).hexdigest(),
            'user': user,
            'date': utc_time_now.strftime('%d/%m/%Y')
        }

        return jwt.encode(
            payload,
            app_config.JWT_SECRET_KEY,
            algorithm = app_config.JWT_ALGORITHM,
            headers = headers
            )


    # Store JWT token
    def request_store(self, ip = None, token = None):
        req_data = {
            'username': 'username',
            'ip_address': ip,
            'jwt': token,
            'timestamp': datetime.datetime.utcnow()
        }
        req = Requests(**req_data)
        db_session.add(req)
        db_session.commit()
        return


    def proxy(self, request = None):
        token = self.jwt_token(user = 'username')
        self.request_store(ip = request.remote_addr, token = token)
        self.logger.info(f'[AuthManager] JWT upstream request: IP {request.remote_addr}, JWT token: {token}')

        headers = dict(request.headers)
        headers.update({ 'x-my-jwt': token })

        response = {}
        try:
            r = requests.post(app_config.UPSTREAM_URL, headers = headers, data = request.get_data())
            try:
                data = r.json()
            except:
                data = {}
            response = {
                'code': r.status_code,
                'data': data
            }
            self.logger.info(f'[AuthManager] JWT upstream response: {response}')
            return response, 200
        except RequestException as e:
            response = {
                'msg': 'API RequestException error'
            }
            self.logger.error(f'[AuthManager] Upstream RequestException error ({str(e)})')
            raise
        except:
            response = {
                'msg': 'API exception error'
            }
            self.logger.error('[AuthManager] Upstream generic exception error')
            raise

        return response, 400


    def echo(self, request = None):
        response = {
            'headers': [ dict(request.headers) ],
            'data': request.get_json()
        }
        return response, 200

