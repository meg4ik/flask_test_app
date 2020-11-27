from flask import Flask, request
from simple_settings import settings
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

app.config.update(**settings.as_dict())


db = SQLAlchemy(app)

class person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable = False)
    job = db.Column(db.String(45))


@app.route("/", methods=["GET","POST"])
def home():
    return "hello", 200

if __name__ == "__main__":
    db.create_all()

    person.query.delete()

    Van = person(name= "Van", age = 3, job = "ATB")
    
    db.session.add(Van)
    db.session.commit()

    app.run()