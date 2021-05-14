from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2000), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    days_to_expire = db.Column(db.Integer, nullable=False, default=90)
    valid_until = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"Url('{self.original_url}', '{self.short_url}', '{self.created_at}', '{self.days_to_expire}')"
