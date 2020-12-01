from main import db

class person(db.Model):
    __tablename__ = 'person'
    idPerson = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable = False)
    job = db.Column(db.String(45), default = None)

    def to_json(self):
        return {
            "id": self.idPerson,
            "name": self.name,
            "age": self.age,
            "job": self.job
        }


class articles(db.Model):
    __tablename__ = 'articles'
    idarticles = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_idPerson = db.Column(db.Integer)
    title = db.Column(db.String(45), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    
    def to_json(self):
        return {
            "idarticles": self.idarticles,
            "title": self.title,
            "content": self.content,
            "person_idPerson": self.person_idPerson
        }