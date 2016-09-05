#coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, current_user
# from flask_nav import Nav
# from flask_nav.elements import *
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name='default'):
	app = Flask(__name__)
	# 读取配置
	app.config.from_object(config[config_name])

	# 初始化db等
	db.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)
	# nav.init_app(app)

	# 注册app蓝图
	from .auth import auth as auth_blueprint
	from .main import main as main_blueprint

	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	app.register_blueprint(main_blueprint)

	# nav.register_element('top', Navbar('Flask', View('主页','main.index')))

	return app