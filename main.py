import streamlit as st

st.title("Happy 1st Wedding Anniversary, My Love, 은순")

def main_page():
    st.markdown("## 당신의 남편은 당신을 진심으로 사랑합니다. 결혼기념일이 조금 지났지만 근사한 식사를 대접하고 싶어합니다.")
    st.write("다음 중 어떤 것을 선택하시겠습니까?")

    if 'btn_accept_clicked' not in st.session_state:
        st.session_state.btn_accept_clicked = True

    if st.button("수락"):
        st.session_state.page = "accept"
        st.session_state.btn_accept_clicked = True
        st.experimental_rerun()

    if st.button("거절"):
        st.session_state.btn_accept_clicked = False
        # st.write("거절은 없습니다.")
    
    if st.session_state.btn_accept_clicked == False:
        st.write("거절은 아니됩니다. 수락을 눌러주세요 ㅠㅠ")

def accept_page():
    if 'selected_date' not in st.session_state:
        # 날짜 선택 기능 추가
        dates = ["2023-10-27", "2023-10-29", "2023-10-30", "2023-11-01", "2023-11-02", "2023-11-05"]
        SELECTED_DATE = st.selectbox("식사 날짜를 선택하세요:", dates)
        st.session_state.selected_date = SELECTED_DATE

        if st.button("날짜 확인"):
            show_map(SELECTED_DATE)

    else:
        show_map(SELECTED_DATE)

def show_map(date):
    st.markdown(f"# {date}에 둘이 오붓하게 식사해요! 제발요... 바로 예약해볼게요!!")

    st.write("만나게 될 장소의 지도입니다:")
    map_code = '''<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3162.5049859902683!2d127.04194717597568!3d37.566724872038556!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357ca4aac8b27bd3%3A0x7538e53249f6fe04!2z67O47JWk67iM66CI65Oc!5e0!3m2!1sko!2skr!4v1697465385271!5m2!1sko!2skr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'''
    st.markdown(map_code, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("# 늦어서 미안해..")
    st.markdown("# 진심으로 고마워..")
    st.markdown("# 그리고 정말 사랑해 ❤️")
    st.write("장모님이랑 가기 싫다고 했을 때, 그냥 나랑 가자고 말할껄 그랬어 ㅠ")

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "accept":
        accept_page()

if __name__ == "__main__":
    main()
