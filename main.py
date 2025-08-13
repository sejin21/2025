import streamlit as st

# 운동 데이터
sports_data = [
    {"name": "요가", "strength": 2, "endurance": 2, "agility": 3, "indoor": True, "team": False},
    {"name": "배드민턴", "strength": 3, "endurance": 3, "agility": 4, "indoor": True, "team": True},
    {"name": "수영", "strength": 4, "endurance": 5, "agility": 3, "indoor": True, "team": False},
    {"name": "농구", "strength": 4, "endurance": 4, "agility": 4, "indoor": True, "team": True},
    {"name": "등산", "strength": 3, "endurance": 5, "agility": 2, "indoor": False, "team": False}
]

st.title("🏋 운동 종목 추천 웹앱")

# 입력 방식 선택
mode = st.radio("체력·기술 입력 방식을 선택하세요", ["직접 입력", "질문으로 측정"])

# ---------------------------
# 1) 직접 입력 모드
# ---------------------------
if mode == "직접 입력":
    strength = st.slider("근력(Strength)", 1, 5, 3)
    endurance = st.slider("지구력(Endurance)", 1, 5, 3)
    agility = st.slider("민첩성(Agility)", 1, 5, 3)

# ---------------------------
# 2) 질문으로 측정 모드
# ---------------------------
else:
    # 근력
    pushups = st.radio("한 번에 팔굽혀펴기를 몇 개 할 수 있나요?", ["0~5개", "6~15개", "16개 이상"])
    strength = 2 if pushups == "0~5개" else (3 if pushups == "6~15개" else 5)

    # 지구력
    jog_time = st.radio("쉬지 않고 조깅할 수 있는 시간은?", ["5분 미만", "5~20분", "20분 이상"])
    endurance = 2 if jog_time == "5분 미만" else (3 if jog_time == "5~20분" else 5)

    # 민첩성
    agility_q = st.radio("방향 전환이 많은 스포츠에서 반응 속도는?", ["느림", "보통", "빠름"])
    agility = 2 if agility_q == "느림" else (3 if agility_q == "보통" else 5)

# 공통 질문 (환경 선호)
indoor_pref = st.radio("실내/실외 선호", ["실내", "실외"])
team_pref = st.radio("개인/팀 선호", ["개인", "팀"])

# ---------------------------
# 추천 알고리즘
# ---------------------------
if st.button("운동 추천 받기"):
    indoor_bool = True if indoor_pref == "실내" else False
    team_bool = True if team_pref == "팀" else False

    recommendations = []
    for sport in sports_data:
        score = 0
        score += 5 - abs(sport["strength"] - strength)
        score += 5 - abs(sport["endurance"] - endurance)
        score += 5 - abs(sport["agility"] - agility)
        if sport["indoor"] == indoor_bool:
            score += 2
        if sport["team"] == team_bool:
            score += 2
        recommendations.append((sport["name"], score))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    st.subheader("추천 운동 종목")
    for rec in recommendations[:3]:
        st.write(f"🏆 {rec[0]} (점수: {rec[1]})")

