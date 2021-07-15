from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import Result


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/result/<url>')
def result(url):
    obj = Result(url,"{'data':'yes'}","{'data':'yes'}")
    db.session.add(obj)
    db.session.commit()    
    return "{}".format(url)


if __name__ == '__main__':
    app.run()

