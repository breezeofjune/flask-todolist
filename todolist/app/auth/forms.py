#coding=utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Length

class LoginForm(Form):
	username = StringField(label='用户名', validators=[DataRequired()])
	password = PasswordField(label='密码', validators=[DataRequired()])
	submit = SubmitField(label='提交')

class RegisterForm(Form):

	email = StringField('邮箱地址', validators=[DataRequired(),
						Length(1, 64),
						Email("邮箱不合法")])

	username = StringField(u'用户名', validators=[DataRequired(),
				Length(1, 64),
				Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
				'用户名必须由字母数、字数、下划线或 . 组成')])

	password = PasswordField(u'密码', validators=[DataRequired(),
				EqualTo('password2', message='密码必须一致')])

	password2 = PasswordField(u'确认密码', validators=[DataRequired()])

	submit = SubmitField(u'马上注册')

