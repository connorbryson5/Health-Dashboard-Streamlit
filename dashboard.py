# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:07:21 2023

@author: Connor
"""

# Libraries

import streamlit as st
import pandas as pd
import plotly.express as px

# Page Layout

st.set_page_config(layout = "wide", initial_sidebar_state= "expanded")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html = True)


st.sidebar.header('Indicators of Heart Disease Dashboard')


# Data
dat = pd.read_csv("https://github.com/connorbryson5/Heart-Disease-Dashboard-Streamlit-/blob/main/data/heart_2022_no_nans.csv?raw=true")


hist1 = px.histogram(dat , x = 'Sex')

# Row A
a1, a2, a3 = st.columns(3)

with a1:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)

with a2:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)


with a3:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)


# Row B
b1, b2, b3 = st.columns(3)

with b1:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)

with b2:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)


with b3:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)



# Row C
c1, c2, c3 = st.columns(3)

#Histogram




with c1:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)

with c2:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)


with c3:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)









