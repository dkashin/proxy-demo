#! /usr/bin/env python3

import unittest, jwt

from proxy.uwsgi import app
from proxy.proxy_jwt.views import _AuthManager

app.testing = True

class JWTTests(unittest.TestCase):

    def test_jwt_encoder(self):
        with app.test_client() as client:
            token = _AuthManager.jwt_token(user = 'test_user')
            self.assertIsInstance(token, str)
        print("TEST: JWT encoder")
        return token

    def test_jwt_decoder(self):
        with app.test_client() as client:
            token_enc = _AuthManager.jwt_token(user = 'test_user')
            self.assertIsInstance(token_enc, str)
            token_dec = jwt.decode(token_enc, options = { 'verify_signature': False })
            self.assertIsInstance(token_dec, dict)
            self.assertIn('user', token_dec)
        print("TEST: JWT decoder")


if __name__ == '__main__':
    unittest.main()
