from flask import Flask, render_template, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def key():
    return render_template('key.html')

@app.route('/grades/<name>', methods=['GET'])
def getStudentGrade(name):
    grades = json.load(open('grades.json'))
    if name in grades:
        return {name: grades[name]}
    
@app.route('/grades', methods=['POST'])
def createNewEntry():
    # request.get_json() converts the JSON obj into Python data
    submit = request.get_json()
    # json.load() take a file obj and returns a JSON obj
    grades = json.load(open('grades.json'))
    grades[submit['name']] = submit['grade']
    # create file pointer
    add_json = open('grades.json', 'w')
    # json.dump() writes Python serialized obj as JSON formatted data into a file
    json.dump(grades, add_json)
    add_json.close()
    return grades

@app.route('/grades/<name>', methods=['PUT'])
def editExistingGrade(name):
    grades = json.load(open('grades.json'))
    if name in grades:
        submit = request.get_json()
        grades[name] = submit['grade']
        add_json = open('grades.json','w')
        json.dump(grades, add_json)
        add_json.close()
        return grades
    
@app.route('/grades/<name>', methods=['DELETE'])
def deleteEntry(name):
    grades = json.load(open('grades.json'))
    if name in grades:
        del grades[name]
        add_json = open('grades.json', 'w')
        json.dump(grades, add_json)
        add_json.close()
        return grades

@app.route('/grades', methods=['GET'])
def allGrades():
    grades = json.load(open('grades.json'))
    return grades


if __name__ == '__main__':
    app.run()