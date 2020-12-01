from flask import Flask, request
from simple_settings import settings
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
try:
    app.config.update(**settings.as_dict())
except:
    print ("Please configurate your environment!")

db = SQLAlchemy(app)

@app.route("/person", methods=["POST","GET"])
def person_fu():
    from models import person
    from forms import PersonForm
    if request.method == "POST":
        form = PersonForm(request.form)
        if form.validate():
            personsql = person(**form.data)
            db.session.add(personsql)
            db.session.commit()
            return "adding!!!", 200
        else:
            return "Form is not valid!", 400 
    else:
        try:
            quotes = person.query.all()
        except Exception as e:
            return str(e)
        else:
            return {"query":[p.to_json() for p in quotes]}

@app.route("/articles", methods=["POST","GET"])
def articles_fu():
    from models import articles
    from forms import ArticlesForm
    if request.method == "POST":
        form = ArticlesForm(request.form)
        if form.validate():
            articlessql = articles(**form.data)
            db.session.add(articlessql)
            db.session.commit()
            return "adding!!!", 200
        else:
            return "Form is not valid!", 400 
    else:
        try:
            quotes = articles.query.all()
        except Exception as e:
            return str(e)
        else:
            return {"query":[p.to_json() for p in quotes]}
        
if __name__ == "__main__":
    from models import *
    db.create_all()
    app.run()