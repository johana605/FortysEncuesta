# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    satisfaction = db.Column(db.Integer, nullable=False)
    recommendation = db.Column(db.String(3), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    comments = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
