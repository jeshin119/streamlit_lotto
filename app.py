import streamlit as st
import random
from datetime import datetime
import time

# 페이지 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎲")

# 세션 상태 초기화
if 'lotto_numbers' not in st.session_state:
    st.session_state.lotto_numbers = []

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중 6개를 무작위로 선택
    numbers = sorted(random.sample(range(1, 46), 6))
    # 현재 시간
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return numbers, current_time

# 타이틀
st.title("🎲 로또 번호 생성기")

# 설명
st.write("아래 버튼을 클릭하면 로또 번호가 생성됩니다. 최대 6개의 번호 세트가 표시됩니다.")

# 번호 생성 버튼
if st.button("로또 번호 생성하기"):
    numbers, current_time = generate_lotto_numbers()
    
    # 새로운 번호를 리스트의 맨 앞에 추가
    st.session_state.lotto_numbers.insert(0, (numbers, current_time))
    
    # 최대 6개까지만 유지
    if len(st.session_state.lotto_numbers) > 6:
        st.session_state.lotto_numbers.pop()

# 생성된 번호들 표시
st.subheader("생성된 번호")
for i, (numbers, time_str) in enumerate(st.session_state.lotto_numbers, 1):
    st.write(f"세트 {i}: {numbers}")
    st.caption(f"생성 시간: {time_str}")
    st.divider()