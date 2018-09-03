from flask import Flask
from config import DevConfig

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)


# 引入各个app中的路由，并注册蓝图
from my_web.todo_app.views import todo_route
from my_web.user_app.views import user_route

app.register_blueprint(todo_route, url_prefix='/')
app.register_blueprint(user_route, url_prefix='/user')
