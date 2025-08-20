import streamlit as st
import random
from pathlib import Path

st.set_page_config(page_title="나만의 운동 코치", page_icon="💪", layout="wide")

# ======================
# 앱 제목
# ======================
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>💪 나만의 운동 코치</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>당신의 목표와 라이프스타일에 맞는 운동을 추천해드립니다!</p>", unsafe_allow_html=True)
st.markdown("---")

# ======================
# 운동 데이터 (영상/로컬 이미지 포함)
# ======================
image_path = Path("images")  # images 폴더 경로

exercise_data = {
    "유산소 운동": {
        "러닝": {
            "난이도": "⭐⭐",
            "설명": "심폐지구력을 기르고 체지방 연소에 효과적인 대표 유산소 운동.",
            "영상": None,
            "이미지": image_path / "running.jpg"
        },
        "점핑잭": {
            "난이도": "⭐⭐",
            "설명": "전신을 사용하는 유산소 운동으로 체지방 감량에 효과적입니다.",
            "영상": "https://www.youtube.com/embed/2W4ZNSwoW_4",
            "이미지": None
        },
        "줄넘기": {
            "난이도": "⭐⭐⭐",
            "설명": "짧은 시간에 칼로리 소모가 큰 운동",
            "영상": "https://www.youtube.com/embed/zgMCV2E34Vo",
            "이미지": None
        }
    },
    "근력 강화": {
        "스쿼트": {
            "난이도": "⭐⭐⭐",
            "설명": "하체 근력을 강화하고 엉덩이와 허벅지 근육을 발달시키는 운동.",
            "영상": "https://www.youtube.com/embed/swRNeYw1JkY",
            "이미지": None
        },
        "푸시업": {
            "난이도": "⭐⭐⭐",
            "설명": "상체 근력 향상에 효과적인 대표적인 운동.",
            "영상": "https://www.youtube.com/embed/iod5dF3Lr6A",
            "이미지": None
        },
        "플랭크": {
            "난이도": "⭐⭐",
            "설명": "코어 근육을 강화하고 전신 안정성을 높이는 운동.",
            "영상": None,
            "이미지": image_path / "plank.jpg"
        },
        "런지": {
            "난이도": "⭐⭐",
            "설명": "허벅지와 엉덩이 근육을 고르게 발달시키는 운동.",
            "영상": None,
            "이미지": image_path / "lunge.jpg"
        }
    },
    "유연성 & 재활": {
        "목 스트레칭": {
            "난이도": "⭐",
            "설명": "목 근육을 풀어주어 긴장 완화와 혈액순환을 돕습니다.",
            "영상": None,
            "이미지": image_path / "neck_stretch.jpg"
        },
        "전신 스트레칭": {
            "난이도": "⭐⭐",
            "설명": "운동 전후로 전신 근육을 풀어주어 부상을 예방합니다.",
            "영상": "https://www.youtube.com/embed/X3-gKPNyrTA",
            "이미지": None
        }
    },
    "요가": {
        "다운독": {
            "난이도": "⭐⭐",
            "설명": "전신 스트레칭 효과와 함께 혈액순환을 촉진하는 요가 자세.",
            "영상": None,
            "이미지": image_path / "down_dog.jpg"
        },
        "나무자세": {
            "난이도": "⭐⭐",
            "설명": "균형감각을 기르고 집중력을 향상시키는 요가 자세.",
            "영상": None,
            "이미지": image_path / "tree_pose.jpg"
        }
    }
}

# ======================
# 질문 폼
# ======================
with st.form("exercise_form"):
    st.subheader("💡 운동 정보를 입력해주세요")

    col1, col2 = st.columns(2)
    with col1:
        목표 = st.selectbox("1️⃣ 운동 목적", ["체중 감량", "체력 강화", "근육 증가", "유연성 향상", "스트레스 해소"])
        운동강도 = st.selectbox("2️⃣ 운동 강도", ["가볍게", "보통", "강하게"])
        시간 = st.selectbox("3️⃣ 하루 운동 가능 시간", ["30분 이하", "30분~1시간", "1시간 이상"])
    with col2:
        실내외 = st.selectbox("4️⃣ 운동 장소", ["실내", "실외", "상관없음"])
        혼자같이 = st.selectbox("5️⃣ 혼자/같이", ["혼자", "같이", "상관없음"])
        관절부담 = st.selectbox("6️⃣ 관절 부담 고려?", ["네", "아니오"])
        장비사용 = st.selectbox("7️⃣ 장비 사용 여부", ["장비 필요 없음", "간단한 장비 가능", "헬스장 기구 사용 가능"])

    submitted = st.form_submit_button("✅ 운동 추천 받기")

# ======================
# 추천 결과 출력
# ======================
if submitted:
    st.subheader("🔥 추천 운동 종목")

    추천운동 = []
    if 목표 == "체중 감량":
        추천운동.extend(list(exercise_data["유산소 운동"].keys()))
    elif 목표 == "체력 강화":
        추천운동.extend(list(exercise_data["근력 강화"].keys()))
    elif 목표 == "근육 증가":
        추천운동.extend(list(exercise_data["근력 강화"].keys()))
    elif 목표 == "유연성 향상":
        추천운동.extend(list(exercise_data["요가"].keys()) + list(exercise_data["유연성 & 재활"].keys()))
    elif 목표 == "스트레스 해소":
        추천운동.extend(list(exercise_data["요가"].keys()) + list(exercise_data["유산소 운동"].keys()))

    추천리스트 = random.sample(추천운동, min(3, len(추천운동)))

    for 운동 in 추천리스트:
        for 카테고리, 운동들 in exercise_data.items():
            if 운동 in 운동들:
                info = 운동들[운동]
                st.markdown(f"""
                <div style='background-color: #F0F8FF; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                    <h3 style='color: #FF4B4B;'>{운동} ({카테고리})</h3>
                    <p><b>난이도:</b> {info['난이도']}</p>
                    <p><b>설명:</b> {info['설명']}</p>
                </div>
                """, unsafe_allow_html=True)

                if info["영상"]:
                    st.video(info["영상"])
                elif info["이미지"]:
                    st.image(str(info["이미지"]), caption=f"{운동} 예시 동작", use_column_width=True)
