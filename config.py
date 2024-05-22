# config.py
import os

class Config:
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///survey.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mssql+pyodbc://appMil:Dannie54!@serverenc.database.windows.net:1433/clientesenc?driver=ODBC+Driver+17+for+SQL+Server'

