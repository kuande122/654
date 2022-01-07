import random
import streamlit as st
confirm_input = st.button('開始遊戲')
confirm_input2 = st.button('輸入確認')
if confirm_input:
  c=random.randint(1,100)
  start=1
  end=100
  x=st.number_input("請輸入%g到%g之間的整數:"%(start,end))
 
  while confirm_input2:
    if x==c:
      st.write("恭喜你中獎了")
    elif x>c:
      if x>=end:
        st.write("輸入不合法,請重新輸入:")
      else:
        end=x
    else:
      if x<=start:
        st.write("輸入不合法,請重新輸入:")
      else:
        start=x

