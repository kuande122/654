import streamlit as st 
import random as RD2

counter =0

max=100
min=1
g=st.number_input('你猜多少?')
target = RD2.randint(min,max)
while True:
  while True:
    g=st.number_input('你猜多少?')
    if g>=min and g<=max :
      break
    else:
      st.write(f'你猜得數需要是{min}到{max}之間')
  counter=counter+1
  if target < g :
    st.write (f'目標比{g}小')
  elif target > g:
    st.write(f'目標比{g}大')
  else :
    st.write (f'你猜中了{target}')
    st.write (f'你總共猜了{counter}次')
    break




