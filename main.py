from flask import Flask, request, jsonify
from simple_settings import settings
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
try:
    app.config.update(**settings.as_dict())
except:
    print ("Please configurate your environment!")

db = SQLAlchemy(app)

class person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable = False)
    job = db.Column(db.String(45))


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        try:
            personsql = person(name = request.form["name"], age = request.form["age"], job = request.form["job"])
            db.session.add(personsql)
            db.session.commit()
        except Exception as e:
            return e, 400
        else:
            return "adding!!!", 200
    else:
        try:
            people = person.query.all()
        except Exception as e:
            return str(e)
        else: return jsonify({"people":[p.to_json() for p in people]})
        

    

if __name__ == "__main__":
    db.create_all()

    app.run()