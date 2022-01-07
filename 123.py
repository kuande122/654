import random
import streamlit as st
confirm_input = st.button('開始遊戲')
if confirm_input:
  a=random.randint(2,99)
  start,end=1,100
  while 1:
    b=st.number_input("請輸入%d到%d之間的整數:"%(start,end))
    if b==a:
      st.write("恭喜你中獎了")
      break
    elif b>a:
      if b>=end:
        st.write("輸入不合法,請重新輸入:")
      else:
        end=b
    else:
      if b<=start:
        write("輸入不合法,請重新輸入:")
      else:
        write=b
if __name__=='__main__':
  paly()

