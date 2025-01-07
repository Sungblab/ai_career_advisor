from flask import Blueprint, render_template, request, jsonify
from app.models.models import User, ChatHistory
from app import db
from sqlalchemy.exc import IntegrityError
from app.utils import get_claude_response

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit_info', methods=['POST'])
def submit_info():
    data = request.json
    user = User(
        name=data['name'],
        age=data['age'],
        grade=data['grade'],
        academic_track=data['academic_track'],
        favorite_subject=data['favorite_subject'],
        disliked_subject=data['disliked_subject'],
        interests=data['interests'],
        hobbies=data['hobbies'],
        career_interests=data['career_interests'],
        mbti=data.get('mbti'),  # Optional field
        strengths=data['strengths'],
        weaknesses=data['weaknesses'],
        extracurricular=data['extracurricular'],
        volunteer=data['volunteer'],
        achievements=data['achievements'],
        academic_performance=data['academic_performance'],
        language_skills=data['language_skills'],
        computer_skills=data['computer_skills'],
        reading_habits=data['reading_habits'],
        role_model=data['role_model'],
        future_job=data['future_job'],
        five_year_goal=data['five_year_goal'],
        stress_management=data['stress_management'],
        learning_style=data['learning_style']
    )
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User info submitted successfully', 'user_id': user.id}), 200
    except IntegrityError:
        db.session.rollback()
        existing_user = User.query.filter_by(name=data['name']).first()
        if existing_user:
            return jsonify({'message': 'User with this name already exists', 'user_id': existing_user.id}), 200
        else:
            return jsonify({'error': 'An error occurred while submitting user info'}), 500

@main.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data['user_id']
    message = data['message']
    api_key = request.headers.get('X-API-Key')
    
    if not api_key:
        return jsonify({'error': 'API key is required'}), 400
    
    # 사용자 정보 가져오기
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    user_info = {
        'name': user.name,
        'age': user.age,
        'grade': user.grade,
        'academic_track': user.academic_track,
        'favorite_subject': user.favorite_subject,
        'disliked_subject': user.disliked_subject,
        'interests': user.interests,
        'hobbies': user.hobbies,
        'career_interests': user.career_interests,
        'mbti': user.mbti,
        'strengths': user.strengths,
        'weaknesses': user.weaknesses,
        'extracurricular': user.extracurricular,
        'volunteer': user.volunteer,
        'achievements': user.achievements,
        'academic_performance': user.academic_performance,
        'language_skills': user.language_skills,
        'computer_skills': user.computer_skills,
        'reading_habits': user.reading_habits,
        'role_model': user.role_model,
        'future_job': user.future_job,
        'five_year_goal': user.five_year_goal,
        'stress_management': user.stress_management,
        'learning_style': user.learning_style
    }
    
    # Claude API 호출 (프롬프트 엔지니어링 적용)
    try:
        response = get_claude_response(user_info, message, api_key)
        
        chat_history = ChatHistory(user_id=user_id, message=message, response=response)
        db.session.add(chat_history)
        db.session.commit()
        
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/privacy')
def privacy():
    return render_template('privacy.html')

@main.route('/terms')
def terms():
    return render_template('terms.html')