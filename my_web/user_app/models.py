from my_web import db

class User(db.Model):
    __tablename__='user_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def save(self):
        db.session.add(self)
        db.session.commit()