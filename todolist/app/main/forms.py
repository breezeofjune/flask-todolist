#coding=utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Length

class AddToDoForm(Form):
	newtodo = StringField(validators=[DataRequired(), Regexp('.*', 0, '有什么需要做')])
	submit = SubmitField('Add')
