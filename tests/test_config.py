#! /usr/bin/env python3

import unittest

from proxy.config import app_config


class ConfigTests(unittest.TestCase):

    def test_jwt_setup(self):
        self.assertIsInstance(app_config.JWT_SECRET_KEY, str)
        self.assertIn('HS512', app_config.JWT_ALGORITHM)
        print('TEST: Config JWT setup')

    def test_upstream_url(self):
        self.assertIn('http', app_config.UPSTREAM_URL)
        print('TEST: Config upstream URL')


if __name__ == '__main__':
    unittest.main()

