from random import randint
import random
import streamlit as st 
#規定範圍並產生密碼
lowest = 1
highest = 100
a = random.randint(lowest, highest)
x=st.number_input("請輸入%g到%g之間的整數:"%(lowest,highest))
st.write(answer)
#重複猜數字，直到猜對為止
while True:
 #判斷有沒有猜中密碼
   if x==a:
     st.write("恭喜你中獎了")
 



