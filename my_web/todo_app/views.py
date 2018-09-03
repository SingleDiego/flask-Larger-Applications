from flask import (
	Blueprint,
	render_template
	)

from my_web.todo_app.models import Todo

todo_route = Blueprint(
	'todo', 
	__name__, 
	template_folder = 'templates'
	)

@todo_route.route('/')
def index():
	todo_list = Todo.query.all()
	return render_template(
		'todo_index.html', 
		todo_list=todo_list
		)