import streamlit as st
def calculate_emi(p, n, r):
  return p*(r/100)*((1+(r/100)**n)/((1+(r/100)**n) - 1))

st.title('EMI Calaculator')
principal = st.sidebar.slider('Principal Loan Amount',1000,100000)
tenure = st.sidebar.slider('Loan Period(in years)',1,30)
n = tenure*12
roi = st.sidebar.slider('Rate of Interest(in % per annum)',1,15)
r = roi/12
if st.sidebar.bottom('Calculate EMI'):
  f'Your EMI is : {calculate_emi(principal, n, r)}'