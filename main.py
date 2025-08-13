import streamlit as st

# 운동 데이터 (이미지 URL, 난이도, 설명 포함)
sports_data = {
    "수영": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Swimming_competition.jpg",
        "difficulty": "중간",
        "description": "전신 근육을 고르게 발달시키고, 관절에 부담이 적은 유산소 운동입니다."
    },
    "마라톤": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/b1/London_marathon.jpg",
        "difficulty": "높음",
        "description": "심폐지구력을 극대화하는 장거리 달리기 운동으로, 강한 체력과 인내심이 필요합니다."
    },
    "요가": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Yoga_class.jpg",
        "difficulty": "낮음",
        "description": "유연성, 균형감각, 정신적 안정에 도움을 주는 저강도 운동입니다."
    },
    "탁구": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Table_tennis_match.jpg",
        "difficulty": "중간",
        "description": "순발력과 집중력을 향상시키는 실내 라켓 스포츠입니다."
    },
    "등산": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/84/Hiking_in_mountains.jpg",
        "difficulty": "중간",
        "description": "심폐지구력과 하체 근력을 강화하며, 자연 속에서 스트레스를 해소할 수 있습니다."
    },
    "배드민턴": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Badminton_game.jpg",
        "difficulty": "중간",
        "description": "민첩성과 순발력을 키울 수 있는 라켓 스포츠입니다."
    },
    "클라이밍": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Indoor_rock_climbing.jpg",
        "difficulty": "높음",
        "description": "상체 근력과 전신 근지구력을 키울 수 있는 도전적인 운동입니다."
    },
    "필라테스": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Pilates_class.jpg",
        "difficulty": "낮음",
        "description": "코어 근육 강화와 자세 개선에 효과적인 운동입니다."
    }
}

st.title("🏋️ 운동 능력 기반 추천 시스템")
st.write("아래 질문에 답하면 당신에게 맞는 운동을 추천해드립니다!")

# 질문 (체력, 기술, 선호 환경, 목표 등)
st.subheader("체력과 운동 습관")
fitness_level = st.selectbox("현재 본인의 체력 수준은?", ["낮음", "중간", "높음"])
technique_level = st.selectbox("운동 기술 수준은?", ["초보", "중급", "고급"])
age = st.number_input("나이를 입력하세요", min_value=10, max_value=100, step=1)

st.subheader("운동 환경 선호도")
environment = st.selectbox("선호하는 운동 환경은?", ["실내", "실외", "상관없음"])
goal = st.selectbox("운동의 주된 목표는?", ["체중 감량", "근육 증가", "유연성 향상", "스트레스 해소", "지구력 향상"])
team_preference = st.selectbox("운동 형태 선호", ["혼자", "팀", "상관없음"])

# 결과 추천 버튼
if st.button("추천받기"):
    recommended_sports = []

    # 간단한 추천 로직
    if goal == "유연성 향상":
        recommended_sports = ["요가", "필라테스"]
    elif goal == "체중 감량":
        if fitness_level == "높음":
            recommended_sports = ["마라톤", "클라이밍"]
        else:
            recommended_sports = ["수영", "등산"]
    elif goal == "근육 증가":
        recommended_sports = ["클라이밍", "필라테스"]
    elif goal == "스트레스 해소":
        if environment == "실내":
            recommended_sports = ["탁구", "배드민턴"]
        else:
            recommended_sports = ["등산", "수영"]
    elif goal == "지구력 향상":
        recommended_sports = ["마라톤", "수영"]

    # 결과 표시
    if recommended_sports:
        st.subheader("추천 운동 종목")
        for sport in recommended_sports:
            data = sports_data[sport]
            st.image(data["image"], caption=sport, use_container_width=True)
            st.write(f"**난이도:** {data['difficulty']}")
            st.write(f"**설명:** {data['description']}")
            st.markdown("---")
    else:
        st.write("조건에 맞는 운동을 찾지 못했습니다. 옵션을 변경해 보세요.")
