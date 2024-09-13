import os

class Config:
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ANTHROPIC_API_KEY = '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'  # 실제 API 키로 교체해주세요