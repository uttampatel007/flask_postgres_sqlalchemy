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
    """
        Just to get the idea of how app.config works ;-)
    """
    context = app.config
    text = "<table>"
    for x in context:
        text += '<tr><td>'+str(x) + '</td><td>' +str(context[x])+'</td></tr>'
    text += "</table>"
    return "<h2>config</h2> <br>{}".format(text)


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/result/<url>')
def result(url):
    """
        Creating Result object and saving it to DB
    """
    obj = Result(url,"{'data':'yes'}","{'data':'yes'}")
    db.session.add(obj)
    db.session.commit()    
    return "{}".format(url)


if __name__ == '__main__':
    app.run()

