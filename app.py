from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    satisfaction = db.Column(db.Integer, nullable=False)
    recommendation = db.Column(db.String(3), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    comments = db.Column(db.Text, nullable=True)

if __name__ == '__main__':
    app.run(debug=True)
