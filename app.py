import streamlit as st
st.title("EC2 Streamlit 배포 성공")
st.write("AWS EC2에서 실행되는 Streamlit 앱입니다.")
name=st.text_input("이름을 입력하세요")
if st.button("확인"):
    print("버튼눌림")
    st.write("버튼 클릭 완료")
    st.success(f"{name}님, EC2 배포 실습 성공")
