import streamlit as st

st.write("You're currently in the Follicular phase!")
st.markdown("Some notes for today: ")

if st.button("Calendar"):
    st.switch_page("pages/calendar.py")
if st.button("Nutrition"):
    st.switch_page("pages/nutrition.py")
if st.button("Symptoms & Mood"):
    st.switch_page("pages/symptoms-mood.py")