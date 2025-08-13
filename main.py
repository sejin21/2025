import streamlit as st

# 운동 데이터 (이름: {난이도, 설명, 이미지URL})
sports_data = {
    "수영": {
        "difficulty": 3,
        "description": "전신 근육을 사용하는 유산소 운동으로, 관절에 부담이 적습니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Swimming_competition.jpg"
    },
    "마라톤": {
        "difficulty": 5,
        "description": "지구력과 정신력을 극한까지 끌어올리는 장거리 달리기 운동입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/54/Marathon_in_São_Paulo.jpg"
    },
    "탁구": {
        "difficulty": 2,
        "description": "빠른 반사신경과 집중력을 키울 수 있는 실내 라켓 스포츠입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Table_tennis_game.jpg"
    },
    "배드민턴": {
        "difficulty": 3,
        "description": "민첩성과 순발력을 기르며 즐길 수 있는 인기 라켓 스포츠입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Badminton_game.jpg"
    },
    "축구": {
        "difficulty": 4,
        "description": "팀워크와 체력을 동시에 요구하는 인기 구기 종목입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Football_in_Brazil.jpg"
    },
    "농구": {
        "difficulty": 4,
        "description": "점프력과 순발력, 협동심을 키우는 대표적인 실내외 구기 운동입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Basketball_game.jpg"
    },
    "등산": {
        "difficulty": 3,
        "description": "자연 속에서 심폐지구력을 기르며 스트레스를 해소할 수 있는 운동입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Hiking_in_the_mountains.jpg"
    },
    "요가": {
        "difficulty": 2,
        "description": "유연성과 균형감을 향상시키며 정신적 안정에도 도움을 줍니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Yoga_Class.jpg"
    },
    "필라테스": {
        "difficulty": 3,
        "description": "코어 근육 강화와 자세 교정에 효과적인 운동입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Pilates_with_small_ball.jpg"
    },
    "스케이트보드": {
        "difficulty": 4,
        "description": "균형감과 순발력을 기르며 창의적인 기술을 즐길 수 있는 익스트림 스포츠입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Skateboard_trick.jpg"
    }
}

st.title("🏋️ 운동 능력 기반 종목 추천 웹앱")

st.write("아래 질문에 답하면 당신에게 맞는 운동 종목을 추천해드립니다!")

# 사용자 입력 질문
st.subheader("1. 체력 수준")
stamina = st.slider("체력을 1~5로 평가하세요 (1: 낮음, 5: 매우 높음)", 1, 5, 3)

st.subheader("2. 기술 수준")
skill = st.slider("운동 기술 수준을 1~5로 평가하세요 (1: 초보, 5: 전문가)", 1, 5, 3)

st.subheader("3. 선호하는 환경")
environment = st.radio("어떤 환경에서 운동하길 좋아하나요?", ["실내", "실외", "상관없음"])

st.subheader("4. 선호하는 운동 강도")
intensity = st.radio("운동 강도를 어떻게 선호하나요?", ["낮음", "중간", "높음"])

# 추천 로직
if st.button("추천 받기"):
    recommendations = []

    for sport, info in sports_data.items():
        score = 0

        # 난이도와 체력 수준이 비슷하면 점수 부여
        score -= abs(info["difficulty"] - stamina)

        # 강도 매칭
        if intensity == "높음" and info["difficulty"] >= 4:
            score += 2
        elif intensity == "중간" and 2 <= info["difficulty"] <= 4:
            score += 2
        elif intensity == "낮음" and info["difficulty"] <= 2:
            score += 2

        # 환경 매칭 (실내/실외)
        if environment == "실내" and sport in ["탁구", "배드민턴", "농구", "요가", "필라테스"]:
            score += 1
        elif environment == "실외" and sport in ["축구", "등산", "마라톤", "스케이트보드", "수영"]:
            score += 1
        elif environment == "상관없음":
            score += 1

        recommendations.append((score, sport))

    recommendations.sort(reverse=True)  # 점수 순 정렬
    best_sport = recommendations[0][1]
    info = sports_data[best_sport]

    # 결과 출력
    st.success(f"추천 종목: **{best_sport}**")
    st.image(info["image"], caption=best_sport, use_column_width=True)
    st.write(f"**난이도:** {info['difficulty']} / 5")
    st.write(f"**설명:** {info['description']}")
