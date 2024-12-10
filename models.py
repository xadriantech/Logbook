from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Entry {self.date}>'
