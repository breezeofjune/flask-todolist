#coding=utf-8
from flask import render_template, redirect, request, flash, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from . import main
from .. import db
from ..models import Todo
from .forms import AddToDoForm


@main.route('/')
@main.route('/index')
def index():
	return render_template('index.html', title='Index')

@main.route('/about')
def about():
	flash('网站提供：')
	flash('Add：增加输入内容为待办事项；')
	flash('Delete删除待办事项，Eidt修改待办事项内容；')
	flash("单选框勾选表示待办事项已完成")
	return render_template('index.html', title='Index')

@main.route('/my_todolist')
@login_required
def my_todolist():

	page_index = request.args.get('page', 1, type=int)
	cur_user_todos = Todo.query.filter_by(author=current_user).order_by(Todo.isdone.asc(),Todo.created.desc())

	pagination = cur_user_todos.paginate(page_index, per_page=5, error_out=False)

	todo_result = pagination.items
	return render_template('main.html', title="My_todo_list",
							todos=todo_result, pagination=pagination)

@main.route('/edit', methods=['POST','GET'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit():

	id = request.args.get('id', 0, type=int)

	if id == 0:
		edittodo = Todo(author=current_user)
		edittodo.isdone = 0
	else:
		edittodo = Todo.query.get_or_404(id)

	#获取ajax传过来的修改内容
	new_content = request.args.get('content')

	edittodo.content = new_content

	db.session.add(edittodo)
	db.session.commit()

	return jsonify(resultmsg='修改成功')

@main.route('/delete_todo', methods=['POST','GET'])
@main.route('/delete_todo/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_todo():
	id = request.args.get('id', 0, type=int)

	marked = Todo.query.get_or_404(id)
	db.session.delete(marked)
	db.session.commit()
	return jsonify(resultmsg='删除成功')

@main.route('/markisdone', methods=['POST','GET'])
@main.route('/markisdone/<int:id>', methods=['GET', 'POST'])
@login_required
def markisdone():
	id = request.args.get('id', 0, type=int)
	isdone = request.args.get('isdone', 0, type=int)

	marked = Todo.query.get_or_404(id)

	marked.isdone = isdone

	#更新操作不需要做add，否则不成功
	# db.session.add(marked)
	db.session.commit()

	return jsonify(resultmsg='修改成功')