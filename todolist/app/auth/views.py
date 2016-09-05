#coding=utf-8
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegisterForm


@auth.route('/login', methods=['GET', 'POST'])
def login():

	login = LoginForm()
	if login.validate_on_submit():
		user = User.query.filter_by(name=login.username.data, password=login.password.data).first()
		if user is not None:
			login_user(user)

			return redirect('/my_todolist')
		else:
			flash('用户名或者密码错误')

	return render_template('login.html', title='登录', form=login)

@auth.route('/register', methods=['GET', 'POST'])
def register():
	register = RegisterForm()
	if register.validate_on_submit():
		user = User(email=register.email.data,
					name=register.username.data,
					password=register.password.data)
		db.session.add(user)
		db.session.commit()
		flash('您已注册成功，请登录！')
		return redirect('/index')
	return render_template('register.html', title='注册', form=register)


@auth.route("/logout")
@login_required
def logout():
	logout_user()
	flash('您已成功登出')
	return redirect('/index')