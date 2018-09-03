from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from my_web import app
from my_web import db

from my_web.todo_app.models import Todo
from my_web.user_app.models import User

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(
        app = app,
        db = db,
        User = User,
        Todo = Todo
        )


if __name__ == '__main__':
    manager.run()
