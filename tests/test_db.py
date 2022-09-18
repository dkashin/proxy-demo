#! /usr/bin/env python3

import unittest, os

from sqlalchemy import func

from proxy.uwsgi import app
from proxy.models import Requests
from proxy.database import db_session, engine


app.testing = True


class DBTests(unittest.TestCase):

    def test_db_connect(self):
        with app.test_client() as client:
            conn = engine.connect()
            status = conn.close()
        print("TEST: DB connect")

    def test_db_count_rec(self):
        with app.test_client() as client:
            counter = Requests.query.with_entities(func.count(Requests.id)).scalar()
            self.assertIsInstance(counter, int)
        print("TEST: DB count records")


if __name__ == '__main__':
    unittest.main()
