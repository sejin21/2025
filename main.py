import streamlit as st

# 샘플 데이터
sports_data = [
    {"name": "요가", "strength": 2, "endurance": 2, "agility": 3, "indoor": True, "team": False},
    {"name": "배드민턴", "strength": 3, "endurance": 3, "agility": 4, "indoor": True, "team": True},
    {"name": "수영", "strength": 4, "endurance": 5, "agility": 3, "indoor": True, "team": False},
    {"name": "농구", "strength": 4, "endurance": 4, "agility": 4, "indoor": True, "team": True},
    {"name": "등산", "strength": 3, "endurance": 5, "agility": 2, "indoor": False, "team": False}
]

st.title("🏋 운동 종목 추천 웹앱")

# 사용자 입력
strength = st.slider("근력(Strength)", 1, 5, 3)
endurance = st.slider("지구력(Endurance)", 1, 5, 3)
agility = st.slider("민첩성(Agility)", 1, 5, 3)
indoor_pref = st.radio("실내/실외 선호", ["실내", "실외"])
team_pref = st.radio("개인/팀 선호", ["개인", "팀"])

if st.button("운동 추천 받기"):
    indoor_bool = True if indoor_pref == "실내" else False
    team_bool = True if team_pref == "팀" else False

    # 점수 계산
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
