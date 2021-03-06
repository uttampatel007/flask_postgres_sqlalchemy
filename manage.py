import os
from flask_script import Manager
from flask_migrate import MigrateCommand

from app import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()