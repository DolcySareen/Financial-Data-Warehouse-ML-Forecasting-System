import unittest
from app import create_app, db

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Redirect to portal
        self.assertIn('/portal', response.headers['Location'])  # Check redirect location

    def test_portal_page(self):
        response = self.client.get('/portal')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AlTraS Portal', response.data)

if __name__ == '__main__':
    unittest.main()