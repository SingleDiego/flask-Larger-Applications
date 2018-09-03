from flask import (
	Blueprint,
	render_template
	)

from my_web.user_app.models import User



user_route = Blueprint(
	'user', 
	__name__, 
	template_folder='templates'
	)

@user_route.route('/')
def index():
	user_list = User.query.all()
	return render_template(
		'user_index.html', 
		user_list=user_list
		)