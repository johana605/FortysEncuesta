from flask_script import Manager
from flask_migrate import Migrate
from app import app, db

manager = Manager(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    manager.run()
