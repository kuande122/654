import random
import streamlit as st
confirm_input = st.button('確認產生答案')

c=random.randint(2,99)
start = 1
end = 100
start,end = 1,100
st.write(c)
x=st.number_input("請輸入%g到%g之間的整數:"%(st.session_state.start,st.session_state.end))
if x==c:
  st.write('恭喜你中獎')
  













