import streamlit as st

def main():
    password = st.text_input('비밀번호 입력', type='password')

    if password:
        st.secrets["user_password"] = password
        st.success("비밀번호가 안전하게 저장되었습니다.")

if __name__ == '__main__':
    main()
