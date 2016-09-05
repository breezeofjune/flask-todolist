import unittest
from flask import url_for
from forgery_py import internet, basic
from app import create_app, db
from app.models import Todo, User

class ModelTest(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_ctx=self.app.app_context()
		self.app_ctx.push()

		self.client = self.app.test_client()

	def tearDown(self):
		self.app_ctx.pop()

	def test_user_role_set(self):
		user = User(name=internet.user_name(),
			email=internet.email_address(),
			password='123')

		db.session.add(user)
		db.session.commit()

		self.assertEqual(user.password, 'Guests')

	def test_index_page(self):
		rep = self.client.get(url_for('main.index'))
		self.assertEqual(rep.status_code, 200)