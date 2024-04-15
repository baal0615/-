import streamlit as st
import time

def mock_login(a,b):
    time.sleep(3)
    return a == 'wujiahui' and b == '123456'

username = st.text_input('Username')
password = st.text_input('Password')

if st.button('Login'):
  with st.spinner('Logging in...'):
   c = mock_login(username,password)
   test ='登录成功'if c else '登录失败'
   st.write(test)
   from PIL import Image
   st.image(Image.open("a2808c7d1bfc9a8a431531d2eda0a6e.jpg"))