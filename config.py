import os

class Config:
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ANTHROPIC_API_KEY = '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'  # 실제 API 키로 교체해주세요