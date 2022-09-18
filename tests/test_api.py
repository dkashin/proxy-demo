#! /usr/bin/env python3

import unittest, json

from proxy.uwsgi import app

app.testing = True

class APITests(unittest.TestCase):

    def test_api_status(self):
        with app.test_client() as client:
            res = client.get('/api/v1/status')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.mimetype, 'text/html')
            self.assertRegex(res.data, b'App is up since')
            self.assertRegex(res.data, b'Total requests processed')
        print("TEST: API GET /api/v1/status")

    def test_api_echo(self):
        with app.test_client() as client:
            data = { "payload": "value"}
            res = client.post(
                '/api/v1/echo',
                data = json.dumps(data),
                content_type = 'application/json'
            )
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.mimetype, 'application/json')
            self.assertRegex(res.data, b'headers')
        print("TEST: API GET /api/v1/echo")

    def test_api_proxy_jwt_payload(self):
        with app.test_client() as client:
            data = { "payload": "value"}
            res = client.post(
                '/api/v1/proxy-jwt',
                data = json.dumps(data),
                content_type = 'application/json'
            )
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.mimetype, 'application/json')
            self.assertRegex(res.data, b'X-My-Jwt')
        print("TEST: API POST /api/v1/proxy-jwt, Case: test payload")

    def test_api_proxy_jwt_payload_empty(self):
        with app.test_client() as client:
            res = client.post('/api/v1/proxy-jwt')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.mimetype, 'application/json')
        print("TEST: API POST /api/v1/proxy-jwt, Case: empty payload")


if __name__ == '__main__':
    unittest.main()
