import logging
from datetime import datetime

from flask import current_app, g

from tests.layouts import DefaultTestCase

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AppTestCase(DefaultTestCase):
    """tests that the app is set up properly"""

    def test_app(self):
        """app is loaded correctly"""
        with self.app.app_context():
            self.assertEqual(self.app, current_app)

    def test_config(self):
        """test that the correct configuration is loaded for tests"""

        self.assertTrue(self.app.testing)
        self.assertFalse(self.app.debug)