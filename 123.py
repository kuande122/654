from random import randint
import streamlit as st 
#規定範圍並產生密碼
lowest = 1
highest = 100
answer = randint(lowest, highest)
x=st.number_input("請輸入%g到%g之間的整數:"%(lowest,highest))
#重複猜數字，直到猜對為止
while True:
    guess = st.write('密碼介於 ' + str(lowest) + '-' + str(highest) + ':\n>>')
 
        #檢查輸入的數字是否介於規定範圍內
    if guess <= lowest or guess >= highest:
        st.write('請輸入 ' + str(lowest) + '-' + str(highest) + ' 之間的整數\n')
        continue
 
        #判斷有沒有猜中密碼
    if guess == answer:
        st.write('答對了！')
        break   #猜對才跳脫迴圈
    elif guess < answer:
        lowest = guess
    else:
        highest = guess

