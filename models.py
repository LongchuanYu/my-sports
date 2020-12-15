from app import db


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8))
    data = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.username
