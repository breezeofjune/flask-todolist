import unittest
import threading
from selenium import webdriver
from app import create_app
import re

class SeleniumTest(unitest.TestCase):
	client = None
	app_ctx = None
	@classmethod
	def setUpClass(cls):
		try:
			cls.client = webdriver.Firefox()
		except Exception, e:
			raise e

		if cls.client:
			cls.create_app('testing')
			cls.app_ctx = cls.app.app_context()
			cls.app_ctx.push()

			threading.Thread(target=cls.app.run).start()

	@classmethod
	def tearDownClass(cls):
		#todo
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

		def test_user_login(self):
			from login_page import LoginPage
			new_user = User(name=internet.user_name(),
				email=internet.email_address(),
				password=basic.text())
			db.session.add(new_user)
			db.session.commit()

			page = LoginPage(self.client)
			self.client.get('http://localhost:5000/auth/login')
			self.assertTrue(u'登录' in page.title)

			page.set_user_name(new_user.name)
			page.set_pwd(new_user.password)
			page.submit()

        # 返回注册结果

        self.assertTrue(re.search(u'欢迎来到Ray的博客', self.client.page_source))
