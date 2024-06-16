import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("Crave")
st.markdown("Crave is more than just a period tracker.")

if st.button("Start"):
    st.switch_page("pages/home.py")