import anthropic
from config import Config

client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)

def engineer_prompt(user_info, user_message):
    prompt = f"""
<h2 style="color: #3498db;">목차</h2>
<ol style="color: #34495e;">
    <li>요약</li>
    <li>학생 프로필</li>
    <li>진로 적합성 분석</li>
    <li>추천 진로 옵션</li>
    <li>교육 및 준비 계획</li>
    <li>실행 전략</li>
    <li>역량 개발 방안</li>
    <li>산업 동향 및 미래 전망</li>
    <li>성격 유형 기반 조언</li>
    <li>학습 및 정신 건강 관리</li>
    <li>결론 및 다음 단계</li>
</ol>

<h2 style="color: #3498db;">1. 요약</h2>
<p style="color: #34495e;">{user_info['name']} 학생의 관심사, 강점, 학업 성취도를 종합적으로 분석한 결과와 주요 권장사항을 간략히 요약해주세요. 현실적이고 달성 가능한 목표를 중심으로 작성해주세요. (3-4문장)</p>

<h2 style="color: #3498db;">2. 학생 프로필</h2>
<table style="width: 100%; border-collapse: collapse; color: #34495e;">
    <tr style="background-color: #3498db; color: white;">
        <th colspan="2">기본 정보</th>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>이름</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['name']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>나이</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['age']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>학년</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['grade']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>계열</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['academic_track']}</td>
    </tr>
    <tr style="background-color: #3498db; color: white;">
        <th colspan="2">학업 및 관심사</th>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>좋아하는 과목</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['favorite_subject']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>싫어하는 과목</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['disliked_subject']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>관심사</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['interests']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>취미</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['hobbies']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>희망 진로</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['career_interests']}</td>
    </tr>
    <tr style="background-color: #3498db; color: white;">
        <th colspan="2">개인 특성</th>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>MBTI</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['mbti']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>강점</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['strengths']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>개선점</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['weaknesses']}</td>
    </tr>
    <tr style="background-color: #3498db; color: white;">
        <th colspan="2">경험 및 성과</th>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>동아리 활동</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['extracurricular']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>봉사활동</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['volunteer']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>주요 성과</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['achievements']}</td>
    </tr>
    <tr style="background-color: #3498db; color: white;">
        <th colspan="2">학업 및 기술</th>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>학업 성취도</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['academic_performance']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>외국어 능력</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['language_skills']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>디지털 역량</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['computer_skills']}</td>
    </tr>
    <tr style="background-color: #3498db; color: white;">
        <th colspan="2">미래 계획</th>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>롤모델</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['role_model']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>장래 희망</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['future_job']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid #bdc3c7; padding: 8px;"><strong>중기 목표 (3년)</strong></td>
        <td style="border: 1px solid #bdc3c7; padding: 8px;">{user_info['five_year_goal']}</td>
    </tr>
</table>

<h2 style="color: #3498db;">3. 진로 적합성 분석</h2>
<p style="color: #34495e;">학생의 관심사, 강점, 개선점, 학업 성취도를 종합적으로 분석하여 진로 적합성을 평가해주세요. 다음 사항을 고려하여 분석해주세요:</p>
<ul style="color: #34495e;">
    <li>학생의 현재 역량과 희망 진로 간의 일치도</li>
    <li>학생의 관심사와 실제 산업 동향의 연관성</li>
    <li>학생의 강점을 살릴 수 있는 진로 옵션</li>
    <li>개선이 필요한 영역과 그에 따른 진로 선택시 고려사항</li>
</ul>
<p style="color: #7f8c8d; font-style: italic;">현실적인 관점에서 학생의 적성과 시장 수요를 균형있게 고려하여 분석해주세요.</p>

<h2 style="color: #3498db;">4. 추천 진로 옵션</h2>
<p style="color: #34495e;">학생에게 적합할 것으로 판단되는 3-5개의 진로 옵션을 제안해주세요. 각 옵션에 대해 다음 정보를 제공해주세요:</p>
<ul style="color: #34495e;">
    <li>진로 설명 및 주요 업무</li>
    <li>필요한 핵심 역량 및 자격</li>
    <li>학생의 현재 강점과 일치하는 부분</li>
    <li>향후 개발이 필요한 영역</li>
    <li>해당 분야의 미래 전망 및 기회 요인</li>
</ul>
<p style="color: #e74c3c; font-weight: bold;">각 진로 옵션에 대해 현실적인 장단점을 제시하고, 학생이 informed decision을 내릴 수 있도록 객관적인 정보를 제공해주세요.</p>

<h2 style="color: #3498db;">5. 교육 및 준비 계획</h2>
<p style="color: #34495e;">추천된 진로를 위한 교육 및 준비 과정을 제시해주세요. 다음 내용을 포함해주세요:</p>
<ul style="color: #34495e;">
    <li>고등학교에서 중점을 두어야 할 과목 및 그 이유</li>
    <li>추천 대학 전공 (2-3개) 및 각 전공의 특징, 장단점</li>
    <li>필요한 자격증 또는 기술 (산업 표준 및 최신 트렌드 반영)</li>
    <li>권장되는 교과 외 활동 및 경험 (인턴십, 프로젝트 등)</li>
    <li>대학 진학 외 대안적 교육 경로 (전문학교, 온라인 교육 등)</li>
</ul>
<p style="color: #7f8c8d; font-style: italic;">4차 산업혁명과 급변하는 직업 환경을 고려하여, 유연성 있는 교육 계획을 수립해주세요.</p>

<h2 style="color: #3498db;">6. 실행 전략</h2>
<p style="color: #34495e;">학생의 현재 상황부터 목표 달성까지의 단계별 실행 전략을 수립해주세요:</p>
<ol style="color: #34495e;">
    <li>단기 목표 (6개월-1년):
        <ul>
            <li>[구체적인 목표 및 실행 계획]</li>
        </ul>
    </li>
    <li>중기 목표 (1-3년):
        <ul>
            <li>[구체적인 목표 및 실행 계획]</li>
        </ul>
    </li>
    <li>장기 목표 (3-5년):
        <ul>
            <li>[구체적인 목표 및 실행 계획]</li>
        </ul>
    </li>
</ol>
<p style="color: #e74c3c; font-weight: bold;">각 단계별 목표는 SMART (Specific, Measurable, Achievable, Relevant, Time-bound) 원칙에 따라 설정해주세요.</p>

<h2 style="color: #3498db;">7. 역량 개발 방안</h2>
<p style="color: #34495e;">제안된 진로에 필요한 핵심 역량을 개발하기 위한 구체적인 방안을 제시해주세요. 다음 내용을 포함해주세요:</p>
<ul style="color: #34495e;">
    <li>추천 온라인 강좌 또는 MOOC (예: Coursera, edX 등의 실제 강좌명 제시)</li>
    <li>실무 경험을 쌓을 수 있는 방법 (예: 관련 분야 아르바이트, 인턴십, 프로젝트 참여 등)</li>
    <li>관련 분야 전문가 멘토링 또는 네트워킹 전략</li>
    <li>자기주도학습을 위한 학습 리소스 및 도구 추천</li>
</ul>
<p style="color: #7f8c8d; font-style: italic;">디지털 시대에 필수적인 데이터 리터러시, 디지털 협업 능력 등 미래 핵심 역량 개발에 중점을 두어주세요.</p>

<h2 style="color: #3498db;">8. 산업 동향 및 미래 전망</h2>
<p style="color: #34495e;">추천된 진로 분야의 현재 동향과 미래 전망에 대해 분석해주세요. 다음 내용을 포함해주세요:</p>
<ul style="color: #34495e;">
    <li>해당 산업의 현재 상황 및 주요 트렌드</li>
    <li>향후 5-10년간의 예상 변화 및 기회 요인</li>
    <li>기술 발전에 따른 직무 변화 예측</li>
    <li>잠재적 위험 요소 및 대비 전략</li>
    <li>국내외 관련 정책 및 제도 변화 전망</li>
</ul>
<p style="color: #e74c3c; font-weight: bold;">신뢰할 수 있는 최신 데이터와 연구 결과를 바탕으로 분석해주세요. 불확실한 정보는 명확히 구분하여 표현해주세요.</p>

<h2 style="color: #3498db;">9. 성격 유형 기반 조언</h2>
<p style="color: #34495e;">학생의 MBTI 유형을 고려하여 다음 사항에 대해 조언해주세요:</p>
<ul style="color: #34495e;">
    <li>해당 MBTI 유형의 강점과 이를 진로에 활용할 수 있는 방법</li>
    <li>잠재적 약점과 이를 보완할 수 있는 전략</li>
    <li>추천 진로 옵션과의 적합성 분석</li>
    <li>효과적인 의사소통 및 협업 방식</li>
    <li>스트레스 관리 및 자기관리 전략</li>
</ul>
<p style="color: #7f8c8d; font-style: italic;">MBTI는 참고 자료로만 활용하고, 개인의 고유한 특성과 상황을 종합적으로 고려하여 조언해주세요.</p>

<h2 style="color: #3498db;">10. 학습 및 정신 건강 관리</h2>
<p style="color: #34495e;">학생의 선호하는 학습 스타일과 현재 상황을 고려하여 다음 사항에 대해 조언해주세요:</p>
<ul style="color: #34495e;">
    <li>효과적인 학습 전략 및 시간 관리 기법</li>
    <li>집중력 향상 및 동기 부여 방법</li>
    <li>스트레스 관리 및 정신 건강 유지를 위한 실천 방안</li>
    <li>건강한 생활 습관 형성을 위한 조언 (운동, 식단, 수면 등)</li>
    <li>학업-삶의 균형을 위한 전략</li>
    <li>디지털 디톡스 및 온라인 활동 관리 방법</li>
</ul>
<p style="color: #e74c3c; font-weight: bold;">학업 성취와 정신 건강의 균형을 강조하고, 지속 가능한 자기 관리 습관 형성에 중점을 두어 조언해주세요.</p>

<h2 style="color: #3498db;">11. 결론 및 다음 단계</h2>
<p style="color: #34495e;">보고서의 주요 내용을 요약하고, 학생의 성공적인 진로 개발을 위한 다음 단계를 제안해주세요:</p>
<ul style="color: #34495e;">
    <li>단기적으로 취해야 할 가장 중요한 행동 3가지</li>
    <li>정기적인 자기 평가 및 목표 조정 방법</li>
    <li>추가 정보나 지원을 받을 수 있는 리소스 (진로 상담 센터, 관련 웹사이트 등)</li>
    <li>향후 진로 탐색 및 결정을 위한 체크리스트</li>
</ul>
<p style="color: #7f8c8d; font-style: italic;">학생이 자신의 진로를 주도적으로 탐색하고 결정할 수 있도록 격려하는 메시지를 포함해주세요.</p>

<p style="color: #34495e;"><strong>사용자 메시지:</strong> {user_message}</p>

<p style="color: #34495e;">위 정보와 지침을 바탕으로 학생에게 맞춤형 진로 상담 보고서를 제공해주세요. 다음 사항에 특히 주의를 기울여 작성해주세요:</p>
<ol style="color: #34495e;">
    <li>현실적이고 실행 가능한 조언: 학생의 현재 상황과 능력을 고려하여 단계적으로 달성 가능한 목표와 전략을 제시해주세요.</li>
    <li>미래 지향적 접근: 4차 산업혁명, 기술 발전, 글로벌화 등 미래 트렌드를 반영한 조언을 제공해주세요.</li>
    <li>다양성 고려: 대학 진학 외에도 다양한 진로 옵션(전문대, 특성화고 졸업 후 취업, 창업 등)을 고려하여 조언해주세요.</li>
    <li>지속적 학습 강조: 빠르게 변화하는 직업 세계에 적응하기 위한 평생학습의 중요성을 강조해주세요.</li>
    <li>정신 건강 및 웰빙: 학업 성취와 함께 정신 건강, 스트레스 관리, 삶의 균형의 중요성을 강조해주세요.</li>
    <li>구체적 리소스 제공: 가능한 한 실제 존재하는 프로그램, 웹사이트, 도구 등을 구체적으로 추천해주세요.</li>
    <li>개인화된 조언: 학생의 고유한 특성, 상황, 선호도를 충분히 반영한 맞춤형 조언을 제공해주세요.</li>
</ol>

<p style="color: #34495e;">보고서는 친근하고 이해하기 쉬운 언어로 작성하되, 전문성 있는 조언을 제공해주세요. 학생이 자신의 잠재력을 발견하고 미래를 준비하는 데 실질적인 도움이 되는 내용을 담아주세요.</p>
"""
    return prompt

def get_claude_response(user_info, user_message):
    system_prompt = """
    당신은 전문적인 고등학생 진로 상담사입니다. 제공된 학생 정보를 바탕으로 상세하고 개인화된 진로 상담 보고서를 작성해주세요. 
    보고서는 구조화되고 전문적인 형식을 갖추어야 하며, 다음 사항을 준수해주세요:

    1. 모든 섹션 제목은 <h2> 태그를 사용하고, 하위 제목은 <h3> 태그를 사용하세요.
    2. 단락은 <p> 태그로 묶어주세요.
    3. 목록은 상황에 따라 <ul> 또는 <ol> 태그를 사용하세요.
    4. 중요한 정보는 <strong> 태그를 사용하여 강조해주세요.
    5. 표가 필요한 경우 <table>, <tr>, <td> 태그를 사용하여 작성해주세요.
    6. 전문 용어나 중요 개념을 설명할 때는 <details>와 <summary> 태그를 활용하여 추가 정보를 제공해주세요.

    보고서는 객관적이고 정확한 정보를 바탕으로 작성하되, 학생 개인의 특성과 상황을 충분히 고려하여 맞춤형 조언을 제공해야 합니다. 다음 사항에 특히 주의를 기울여 주세요:

    - 학생의 관심사, 강점, 약점을 종합적으로 분석하여 가장 적합한 진로 방향을 제시하세요.
    - 현실적이고 달성 가능한 단기, 중기, 장기 목표를 설정하고, 각 목표에 대한 구체적인 실행 계획을 제안하세요.
    - 추천하는 직업군이나 학업 경로에 대해 장단점을 균형 있게 제시하고, 잠재적인 어려움과 그 극복 방안도 함께 언급하세요.
    - 학생의 MBTI 유형과 선호하는 학습 스타일을 고려하여 개인화된 학습 및 발전 전략을 제안하세요.
    - 최신 산업 동향과 미래 전망을 반영하여 조언을 제공하되, 불확실한 정보는 명확히 구분하여 표현하세요.
    - 학생의 스트레스 관리와 정신 건강의 중요성을 강조하고, 이를 위한 실질적인 조언을 제공하세요.
    - 필요한 경우, 추가 정보나 상담이 필요한 영역을 명시하고 구체적인 질문을 제시하세요.

    보고서는 전문성과 함께 따뜻하고 격려하는 톤을 유지하여, 학생이 자신의 잠재력을 최대한 발휘할 수 있도록 동기를 부여해야 합니다. 마지막으로, 보고서의 모든 내용이 윤리적이고 편견 없는 조언을 제공하도록 주의를 기울여 주세요.
    """

    engineered_prompt = engineer_prompt(user_info, user_message)

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=5000,
        temperature=0.7,
        system=system_prompt,
        messages=[
            {"role": "user", "content": engineered_prompt}
        ]
    )
    return message.content[0].text