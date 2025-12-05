from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20))  # 'admin', 'doctor', 'researcher'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Storing medical data as JSON to be flexible with different datasets
    medical_data = db.Column(db.JSON)
    
    doctor = db.relationship('User', backref='patients')

class SyntheticData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=True)
    dataset_name = db.Column(db.String(100)) # e.g., 'heart_disease', 'diabetes'
    generated_data = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
