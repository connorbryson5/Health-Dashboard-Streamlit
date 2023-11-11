# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:07:21 2023

@author: Connor
"""

# Libraries

import streamlit as st
import pandas as pd
import plost

# Page Layout

st.set_page_config(layout = "wide", initial_sidebar_state= "expanded")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html = True)


st.sidebar.header('Indicators of Heart Disease Dashboard')


# Data
dat = pd.read_csv("C:/Users/Connor/Desktop/Intro to Informatics/Projects/Heart-Disease-Dashboard-Streamlit-/data/heart_2022_no_nans.csv")

dat.head()

dat.columns


# Row A
a1, a2, a3 = st.columns(3)

# Row B
b1, b2, b3 = st.columns(3)


# Row C
c1, c2, c3 = st.columns((5,5))

with c1:
    st.markdown('### Bar chart')
    plost.bar_chart(dat, 
                    value = 'HeightInMeters',
                    color = 'CovidPos')













