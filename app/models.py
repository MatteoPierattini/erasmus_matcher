from app import db

class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', backref='university', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    syllabus = db.Column(db.Text, nullable=False)
    embedding = db.Column(db.PickleType, nullable=True) 
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
