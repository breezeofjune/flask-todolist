#coding=utf-8
from flask_script import Manager, Shell
from app import create_app, db
from app.models import User, Role, Todo
from flask_migrate import Migrate, MigrateCommand, upgrade


app = create_app('default')
print(type(app))
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def dev():
	from livereload import Server
	live_server = Server(app.wsgi_app)
	live_server.watch('**/*.*')
	live_server.serve(open_url=False)

@manager.command
def forged():

	# 注意：由于python3将xrange去掉，所以需要将安装的forgery_py\forgery\basic.py", line 73的xrange改为range
	from forgery_py import basic, lorem_ipsum, name, internet, date
	from random import randint

	db.drop_all()
	db.create_all()

	Role.seed()
	guests = Role.query.first()

	def generate_todo(func_boolean, func_author):
		return Todo(content=lorem_ipsum.sentences(),
					created=date.date(past=True),
					isdone=func_boolean(),
					author=func_author())

	def generate_user():
		return User(name=internet.user_name(),
					email=internet.email_address(),
					password=basic.text(6, at_least=6, spaces=False),
					role=guests)



	users = [generate_user() for i in range(0,5)]
	db.session.add_all(users)

	booleans = [0,1]
	random_user = lambda:users[randint(0, 4)]
	random_boolean = lambda:booleans[randint(0,1)]
	todos = [generate_todo(random_boolean, random_user) for i in range(0,100)]
	db.session.add_all(todos)

	db.session.commit()

@manager.command
def test():
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	manager.run()