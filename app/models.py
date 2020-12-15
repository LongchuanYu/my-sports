from app import db


class MyData(db.Model):
    __tablename__ = 'mydata'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8))
    data = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.username
