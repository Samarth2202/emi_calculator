import streamlit as st
@st.cache()
def calculate_emi(p, n, r):
  return p*(r/100)*((1+(r/100)**n)/((1+(r/100)**n) - 1))

st.title("EMI Calaculator")
