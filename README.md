# AI 기반 고등학생 진로 탐색 서비스

## 프로젝트 소개

이 서비스는 Claude AI를 활용하여 고등학생들에게 맞춤형 진로 상담을 제공하는 웹 애플리케이션입니다. 학생들의 학업 성취도, 관심사, MBTI, 취미 등 다양한 정보를 종합적으로 분석하여 개인화된 진로 상담을 제공합니다.

## 주요 기능

- 사용자 정보 입력 (7단계)
  - 기본 정보
  - 학업 정보
  - 진로 및 관심사
  - 활동 및 경험
  - 성격 및 특성
  - 학업 및 기술
  - 미래 계획 및 목표
- AI 기반 진로 상담
- 실시간 채팅 인터페이스
- 맞춤형 진로 추천
- 구체적인 실천 계획 제시

## 기술 스택

- Backend: Flask
- Database: SQLite
- AI: Anthropic Claude API
- Frontend: HTML, TailwindCSS, JavaScript
- 폰트: Noto Sans KR

## 설치 방법 (Anaconda 환경)

1. Anaconda 설치

   - [Anaconda 공식 사이트](https://www.anaconda.com/download)에서 다운로드 및 설치

2. 아나콘다 가상환경 생성 및 활성화

   ```bash
   conda create -n career-ai python=3.9
   conda activate career-ai
   ```

3. 저장소 클론

   ```bash
   git clone [repository-url]
   cd project
   ```

4. 의존성 설치

   ```bash
   pip install -r requirements.txt
   ```

5. 환경 변수 설정

   - `.env` 파일에 다음 내용 추가:

   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   ```

6. 데이터베이스 초기화

   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

7. 서버 실행
   ```bash
   python run.py
   ```

## 사용 방법

### 1. API 키 설정

- [Anthropic Console](https://console.anthropic.com/)에서 API 키 발급
- 웹 인터페이스의 "API 키 설정" 버튼을 클릭하여 발급받은 API 키 입력

### 2. 사용자 정보 입력

- 7단계에 걸쳐 상세 정보를 입력
- 각 단계별로 제공되는 예시를 참고하여 작성
- 모든 필수 항목을 빠짐없이 입력

### 3. AI 상담

- 입력된 정보를 바탕으로 AI와 실시간 상담 진행
- 진로, 학업, 적성 등에 대해 자유롭게 질문
- AI의 분석과 조언을 통해 진로 방향 설정

## 주요 파일 구조

project/
├── app/
│ ├── templates/
│ │ ├── index.html
│ │ ├── privacy.html
│ │ └── terms.html
│ ├── models/
│ │ └── models.py
│ ├── routes/
│ │ └── main.py
│ ├── utils.py
│ └── init.py
├── config.py
├── requirements.txt
├── run.py
└── README.md

## 보안 및 주의사항

- API 키 관리

  - API 키는 절대 공개되거나 공유되어서는 안 됨
  - 키는 클라이언트 측에서 안전하게 저장됨
  - 주기적인 키 갱신 권장

- 개인정보 보호

  - 입력된 개인정보는 상담 목적으로만 사용
  - 세션 종료 후 모든 정보는 자동 삭제
  - 민감한 개인정보 입력 자제

- 서비스 이용
  - AI 상담은 참고용으로만 활용
  - 중요한 진로 결정은 전문 상담사와 상담 권장
  - 서비스 이용 중 발생하는 문제는 개발자에게 즉시 보고

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 연락처

- 이메일: sungblab@gmail.com
- 블로그: [https://sungblab.vercel.app](https://sungblab.vercel.app)

## 기여 방법

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 업데이트 내역

- 1.0.0
  - 최초 릴리즈
