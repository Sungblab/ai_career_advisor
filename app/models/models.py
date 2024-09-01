from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    academic_track = db.Column(db.String(64))
    favorite_subject = db.Column(db.String(128))
    disliked_subject = db.Column(db.String(128))
    interests = db.Column(db.String(256))
    hobbies = db.Column(db.String(256))
    career_interests = db.Column(db.String(256))
    mbti = db.Column(db.String(4))
    strengths = db.Column(db.String(256))
    weaknesses = db.Column(db.String(256))
    extracurricular = db.Column(db.String(256))
    volunteer = db.Column(db.Text)
    achievements = db.Column(db.Text)
    academic_performance = db.Column(db.String(64))
    language_skills = db.Column(db.String(256))
    computer_skills = db.Column(db.String(256))
    reading_habits = db.Column(db.String(256))
    role_model = db.Column(db.String(128))
    future_job = db.Column(db.String(128))
    five_year_goal = db.Column(db.Text)
    stress_management = db.Column(db.String(256))
    learning_style = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('chat_history', lazy=True))