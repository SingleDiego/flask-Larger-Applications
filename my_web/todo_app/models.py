from my_web import db

class Todo(db.Model):
    __tablename__='todo_table'

    id = db.Column(db.Integer, primary_key=True)
    work = db.Column(db.String(80))

    def save(self):
        db.session.add(self)
        db.session.commit()