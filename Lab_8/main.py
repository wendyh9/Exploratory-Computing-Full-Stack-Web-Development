from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from itertools import zip_longest
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.secret_key = os.urandom(24)
db = SQLAlchemy(app)


class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    Name = db.Column(db.String(80), nullable=False)
    class_relation = db.relationship('classes', backref='Teacher', lazy=True)


class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    Name = db.Column(db.String(80), unique = True, nullable=False)
    enrollment = db.relationship('enrollment', backref='Student', lazy=True)

class enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(80), db.ForeignKey('student.Name'))
    class_name = db.Column(db.String(80), db.ForeignKey('classes.Name'))
    grade = db.Column(db.Float)

class classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher_name = db.Column(db.String(80), nullable=False)
    enrollment = db.relationship('enrollment', backref='Classes', lazy=True)
    capacity = db.Column(db.Integer)

@app.route('/std/<id>', methods=['DELETE'])
def delete_student(id):
    db.session.delete(student.query.filter_by(Name=id).first())
    db.session.commit()
    return 'Done'


@app.route('/teach/<id>', methods=['DELETE'])
def delete_teacher(id):
    db.session.delete(teacher.query.filter_by(Name=id).first())
    db.session.commit()
    return 'Done'

@app.route('/classes/<id>', methods=['DELETE'])
def delete_class(id):
    db.session.delete(classes.query.filter_by(Name=id).first())
    db.session.commit()
    return 'Done'




@app.route('/classes/<id>', methods = ['PUT'])
def change_Teach(id):
    submission = request.get_json()
    nuTeach = submission['teach']
    Tc = classes.query.filter_by(Name=id)
    Tc = Tc.update(dict(teacher_name=nuTeach))
    db.session.commit()

    return 'Done'

@app.route('/std/' , methods = ['POST'])
def new_Student():
    submission = request.get_json()
    Usnam = submission["student_username"]
    spass = submission["student_password"]
    snam = submission["student_name"]
    Ns = student( username = Usnam, password = spass, Name =snam)
    db.session.add(Ns)
    db.session.commit()
    return 'Done'

@app.route('/admin/' , methods = ['POST'])
def new_Admin():
    submission = request.get_json()
    adminUsname = submission["admin_username"]
    adminPassword = submission["admin_password"]
    Na = admin(username = adminUsname, password = adminPassword)
    db.session.add(Na)
    db.session.commit()
    return 'Done'

@app.route('/teach/' , methods = ['POST'])
def new_Teach():
    submission = request.get_json()
    teachUsnam = submission["teacher_username"]
    teachPassword = submission["teacher_password"]
    teachName = submission["new_teacher_name"]
    Nt = teacher( username = teachUsnam, password = teachPassword, Name =teachName)
    db.session.add(Nt)
    db.session.commit()
    return 'Done'

@app.route('/classes/' , methods = ['POST'])
def new_Class():
   submission = request.get_json()
   className = submission["class_name"]
   classTeacher = submission["class_teacher"]
   # tID = teacher.id.query.filter_by(Name = "class_teacher")
   Nc = classes(Name = className, teacher_name = classTeacher, capacity =30 )
   db.session.add(Nc)
   db.session.commit()

   return 'Done'


@app.route('/grades/' , methods = ['POST'])
def new_Enrolled_Student():
    submission = request.get_json()
    enrolled_class_name = submission["cnaam"]
    enrollee_name = submission["nsname"]
    Nes = enrollment(class_name = enrolled_class_name, student_name = enrollee_name)
    db.session.add(Nes)
    db.session.commit()

    return 'Done'

@app.route('/grades/<id>', methods = ['PUT'])
def change_Grade(id):
    submission = request.get_json()
    classCheck = submission['cgradename']
    newClassGrade = submission['newgrae']
    Ng = enrollment.query.filter_by(student_name = id,class_name = classCheck)
    Ng = Ng.update(dict(grade=newClassGrade))
    db.session.commit()
    return 'Done'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username exists in the database
    user_admin = admin.query.filter_by(username=username).first()
    user_teacher = teacher.query.filter_by(username=username).first()
    user_student = student.query.filter_by(username=username).first()

    if user_admin:
        if user_admin.password == password:
            return render_template('admin.html')
        else:
            return render_template('index.html', error=True)

    elif user_teacher:
        if user_teacher.password == password:
            return redirect(url_for('teacher_view', name = user_teacher.Name))
        else:
            return render_template('index.html', error=True)

    elif user_student:
        if user_student.password == password:
            return redirect(url_for('student_view', name=user_student.Name))
        else:
            return render_template('index.html', error=True)
    else:
        return render_template('index.html', error=True)
    
@app.route('/std/<id>', methods=['DELETE'])
def delete_student(id):
    db.session.delete(student.query.filter_by(Name=id).first())
    db.session.commit()
    return 'Done'


@app.route('/teach/<id>', methods=['DELETE'])
def delete_teacher(id):
    db.session.delete(teacher.query.filter_by(Name=id).first())
    db.session.commit()
    return 'Done'

@app.route('/classes/<id>', methods=['DELETE'])
def delete_class(id):
    db.session.delete(classes.query.filter_by(Name=id).first())
    db.session.commit()
    return 'Done'




@app.route('/classes/<id>', methods = ['PUT'])
def change_Teach(id):
    submission = request.get_json()
    nuTeach = submission['teach']
    Tc = classes.query.filter_by(Name=id)
    Tc = Tc.update(dict(teacher_name=nuTeach))
    db.session.commit()

    return 'Done'

@app.route('/std/' , methods = ['POST'])
def new_Student():
    submission = request.get_json()
    Usnam = submission["student_username"]
    spass = submission["student_password"]
    snam = submission["student_name"]
    Ns = student( username = Usnam, password = spass, Name =snam)
    db.session.add(Ns)
    db.session.commit()
    return 'Done'

@app.route('/admin/' , methods = ['POST'])
def new_Admin():
    submission = request.get_json()
    adminUsname = submission["admin_username"]
    adminPassword = submission["admin_password"]
    Na = admin(username = adminUsname, password = adminPassword)
    db.session.add(Na)
    db.session.commit()
    return 'Done'

@app.route('/teach/' , methods = ['POST'])
def new_Teach():
    submission = request.get_json()
    teachUsnam = submission["teacher_username"]
    teachPassword = submission["teacher_password"]
    teachName = submission["new_teacher_name"]
    Nt = teacher( username = teachUsnam, password = teachPassword, Name =teachName)
    db.session.add(Nt)
    db.session.commit()
    return 'Done'

@app.route('/classes/' , methods = ['POST'])
def new_Class():
   submission = request.get_json()
   className = submission["class_name"]
   classTeacher = submission["class_teacher"]
   # tID = teacher.id.query.filter_by(Name = "class_teacher")
   Nc = classes(Name = className, teacher_name = classTeacher, capacity =30 )
   db.session.add(Nc)
   db.session.commit()

   return 'Done'


@app.route('/grades/' , methods = ['POST'])
def new_Enrolled_Student():
    submission = request.get_json()
    enrolled_class_name = submission["cnaam"]
    enrollee_name = submission["nsname"]
    Nes = enrollment(class_name = enrolled_class_name, student_name = enrollee_name)
    db.session.add(Nes)
    db.session.commit()

    return 'Done'

@app.route('/grades/<id>', methods = ['PUT'])
def change_Grade(id):
    submission = request.get_json()
    classCheck = submission['cgradename']
    newClassGrade = submission['newgrae']
    Ng = enrollment.query.filter_by(student_name = id,class_name = classCheck)
    Ng = Ng.update(dict(grade=newClassGrade))
    db.session.commit()
    return 'Done'








@app.route('/login/student/<name>')
def student_view(name):
    current_student = student.query.filter_by(Name = name).first()
    all_classes = classes.query.all()
    enrolled_classes = [enrollment.Classes for enrollment in current_student.enrollment]
    available_classes = [avail_class for avail_class in all_classes if avail_class not in enrolled_classes]
    return render_template('student.html', Name=current_student.Name, available_classes = available_classes, enrolled_classes = enrolled_classes)


@app.route('/login/teacher/<name>')
def teacher_view(name):
    current_teacher = teacher.query.filter_by(Name=name).first()
    all_classes = classes.query.all()
    taught_classes = [teaching for teaching in all_classes if teaching.teacher_name == current_teacher.Name]
    students_enrolled = [(enrollment.Student.Name for enrollment in enrollment.query.filter_by(class_name=teaching.Name).all()) for teaching in taught_classes]
    return render_template('teacher.html', Name=current_teacher.Name, taught_classes=taught_classes, students_enrolled=students_enrolled)



@app.route('/drop/<id>/<id2>', methods=['DELETE'])
def drop_class(id, id2):
    class_to_drop = enrollment.query.filter_by(class_name=id, student_name = id2 ).first()
    if class_to_drop and class_to_drop != 0:
        db.session.delete(class_to_drop)
        db.session.commit()
        return render_template('index.html', success_drop = True)


@app.route('/enroll/<class_name>/<user_name>', methods=['POST'])
def enroll_class(class_name, user_name):
    existing_enrollment = enrollment.query.filter_by(student_name=user_name, class_name=class_name).first()
    if existing_enrollment:
        # Enrollment already exists, show an error message
        flash('You are already enrolled in {}!'.format(existing_enrollment.class_name))
        return url_for('student_view', name=user_name)
    else:
        # Add new enrollment to the database
        length_enrollment = enrollment.query.filter_by(class_name = class_name).count()
        class_capacity = classes.query.filter_by(Name = class_name).first()
        if length_enrollment >= class_capacity.capacity:
            return url_for('student_view', name=user_name)
        else:
            class_to_enroll = enrollment(student_name=user_name, class_name=class_name, grade = 0)
            db.session.add(class_to_enroll)
            db.session.commit()
            # Redirect to the student view with a success message
            flash('You have successfully enrolled in {}!'.format(class_to_enroll.class_name))
            return url_for('student_view', name=user_name)



@app.route('/teacher/enrolled_students/<class_id>')
def enrolled_students(class_id):
    current_class = classes.query.get(class_id)
    enrollments = enrollment.query.filter_by(class_name=current_class.Name).all()
    students_enrolled = [enrollment.Student for enrollment in enrollments]
    students_grade = [enrollment.grade for enrollment in enrollments]
    student_grade_pairs = zip(students_enrolled, students_grade)
    return render_template('enrolled_students.html', class_name=current_class.Name, student_grade_pairs=student_grade_pairs, Name = current_class.teacher_name )


@app.route('/update/<class_name>/<student_name>', methods=['PUT'])
def update_grade(class_name, student_name):
    submission = request.get_json()
    NewGrade = submission['grade']
    Enrollment = enrollment.query.filter_by(student_name = student_name, class_name = class_name).first()
    Enrollment.grade = NewGrade
    db.session.commit()
    return "Grade updated successfully"

    




if __name__ == '__main__':
    app.run()


