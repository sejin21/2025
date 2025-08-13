import streamlit as st

st.set_page_config(page_title="운동 종목 추천", page_icon="🏋️", layout="wide")

st.title("🏋️ 운동 능력 기반 맞춤 종목 추천")
st.write("당신의 체력, 기술, 성향을 바탕으로 어울리는 운동 종목을 추천해드립니다.")

# ---------------------------
# 1. 질문 섹션
# ---------------------------
st.header("📋 자기 진단 질문")

체력 = st.slider("당신의 전반적인 체력 수준은 어느 정도입니까? (1=매우 낮음, 10=매우 높음)", 1, 10, 5)
지구력 = st.slider("오래 버티는 지구력은 어느 정도입니까?", 1, 10, 5)
민첩성 = st.slider("순발력과 민첩성은 어느 정도입니까?", 1, 10, 5)
협응력 = st.slider("눈과 손, 몸의 협응력은 어느 정도입니까?", 1, 10, 5)
팀플레이 = st.selectbox("개인 운동과 단체 운동 중 어느 것을 선호합니까?", ["개인", "단체", "둘 다 상관없음"])
실내외 = st.selectbox("실내 운동과 실외 운동 중 어느 것을 선호합니까?", ["실내", "실외", "둘 다 상관없음"])
목표 = st.selectbox("운동 목적은 무엇입니까?", ["건강 유지", "체중 감량", "근육 증가", "취미/재미", "경쟁/대회"])

# ---------------------------
# 2. 운동 종목 데이터
# ---------------------------
운동_데이터 = [
    {
        "이름": "수영",
        "난이도": "중",
        "설명": "전신 근육을 사용하는 유산소 및 근력 운동. 관절에 부담이 적고 체력, 지구력 향상에 좋음.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Swimming.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: c>=4 and t>=4 and io in ["실내", "둘 다 상관없음"]
    },
    {
        "이름": "마라톤",
        "난이도": "상",
        "설명": "장거리 달리기. 강한 지구력과 꾸준한 훈련이 필요하며, 체중 감량과 심폐지구력 향상에 효과적.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/0/09/Marathon_in_Tokyo.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: t>=7 and io in ["실외", "둘 다 상관없음"]
    },
    {
        "이름": "요가",
        "난이도": "하",
        "설명": "유연성과 균형감 향상, 스트레스 완화에 탁월. 남녀노소 모두 가능.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Yoga_Pose.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: io in ["실내", "둘 다 상관없음"]
    },
    {
        "이름": "축구",
        "난이도": "중",
        "설명": "순발력, 민첩성, 팀워크가 중요한 대표적인 단체 스포츠.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Soccer_game.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: a>=5 and tm in ["단체", "둘 다 상관없음"]
    },
    {
        "이름": "클라이밍",
        "난이도": "상",
        "설명": "상체 근력, 하체 힘, 집중력과 도전 정신이 필요한 스포츠.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Indoor_Climbing.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: c>=6 and h>=5
    },
    {
        "이름": "탁구",
        "난이도": "중",
        "설명": "빠른 반사신경과 손-눈 협응력, 집중력이 필요한 실내 스포츠.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Table_tennis_paddles.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: h>=6 and io in ["실내", "둘 다 상관없음"]
    },
    {
        "이름": "등산",
        "난이도": "중",
        "설명": "자연 속에서 심폐지구력과 하체 근력을 동시에 기를 수 있는 운동.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Hiking_in_Korea.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: t>=5 and io in ["실외", "둘 다 상관없음"]
    },
    {
        "이름": "복싱",
        "난이도": "상",
        "설명": "전신 근육 강화, 순발력, 체력, 집중력 향상에 좋은 격투 스포츠.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Boxing_in_progress.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: c>=6 and a>=6
    },
    {
        "이름": "배드민턴",
        "난이도": "중",
        "설명": "빠른 스텝과 순발력, 민첩성이 요구되는 라켓 스포츠.",
        "이미지": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Badminton_rally.jpg",
        "조건": lambda c,t,a,h,tm,io,goal: a>=5 and io in ["실내", "둘 다 상관없음"]
    }
]

# ---------------------------
# 3. 추천 로직
# ---------------------------
추천_종목 = []
for 운동 in 운동_데이터:
    if 운동["조건"](체력, 지구력, 민첩성, 협응력, 팀플레이, 실내외, 목표):
        추천_종목.append(운동)

# ---------------------------
# 4. 결과 출력
# ---------------------------
st.header("🏆 추천 운동 종목")

if 추천_종목:
    for 운동 in 추천_종목:
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(운동["이미지"], use_container_width=True)
            with col2:
                st.subheader(f"{운동['이름']} ({운동['난이도']})")
                st.write(운동["설명"])
            st.markdown("---")
else:
    st.warning("조건에 맞는 운동 종목이 없습니다. 입력 값을 조정해 보세요!")
