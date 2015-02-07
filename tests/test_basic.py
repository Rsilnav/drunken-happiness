# tests/test_basic.py

import unittest

from base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page requires user login
    def test_home(self):
        response = self.client.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that welcome page loads
    def test_login(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
