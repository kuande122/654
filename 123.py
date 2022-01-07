import random
import streamlit as st
confirm_input = st.button('開始遊戲')
confirm_input1 = st.button('輸入確認')
if confirm_input:
  a=random.randint(2,99)
  start,end=1,100
  b=st.number_input("請輸入%d到%d之間的整數:"%(start,end))
  if confirm_input1 :
    st.write('人')
    if b:
      if b==a:
       st.write("恭喜你中獎了")
    
    elif b>a:
      if b>=end:
        st.write("輸入不合法,請重新輸入:")
      else:
       end=b
    else:
      if b<=start:
        st.write("輸入不合法,請重新輸入:")
      else:
        st.write=b
#if __name__=='__main__':
  #paly()

