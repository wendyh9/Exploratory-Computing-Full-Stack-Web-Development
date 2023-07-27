from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# import json

app = Flask(__name__)

# use .app_context to create the application context
with app.app_context():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
    # use SQLAlchemy as ORM
    db = SQLAlchemy(app)
    CORS(app)
    class studentClass(db.Model):
        # define columns of database
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, nullable=False, unique=True)
        grade = db.Column(db.Float, nullable=False, unique=False)
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade
    # use .create_all() to create foreign key constraints between tables usually inline with the table definition itself
    db.create_all()

def createJson(studentClass):
    json = {}
    for student in studentClass:
        # create new entries and maps name with grade
        json.update({student.name:student.grade})
    return json


@app.route('/')
def key():
    return render_template('key.html')

@app.route('/grades/<id>', methods=['GET'])
def getStudentGrade(id):
    return createJson(studentClass.query.filter_by(name=id))
    
@app.route('/grades', methods=['POST'])
def createNewEntry():
    newEntry = request.get_json()
    name = newEntry['name']
    grade = newEntry['grade']
    student = studentClass(name, grade)
    db.session.add(student)
    # commit the changes made using commit() method
    db.session.commit()
    return {name:grade}

@app.route('/grades/<id>', methods=['PUT'])
def editExistingGrade(id):
    existing = request.get_json()
    newGrade = existing['grade'] 
    student = studentClass.query.filter_by(name=id)
    student = student.update(dict(grade=newGrade))
    # commit the changes made using commit() method
    db.session.commit()
    return createJson(studentClass.query.all())
    
@app.route('/grades/<id>', methods=['DELETE'])
def deleteEntry(id):
    # delete first entry that has name 
    db.session.delete(studentClass.query.filter_by(name=id).first())
    # commit the changes made using commit() method
    db.session.commit()
    return createJson(studentClass.query.all())

@app.route('/grades', methods=['GET'])
def allGrades():
    return createJson(studentClass.query.all())


if __name__ == '__main__':
    app.run()