# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:07:21 2023

@author: Connor Bryson
"""

# Libraries

import streamlit as st
import pandas as pd
import plotly.express as px

# Page Layout

st.set_page_config(layout = "wide", initial_sidebar_state= "expanded")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html = True)


## Sidebar
st.sidebar.header('Indicators of Heart Disease Dashboard')



# Caching data
@st.cache_data
def get_data(filename):
    dat = pd.read_csv(filename)
    return dat

# Data
dat = get_data("C:/Users/Connor/Desktop/Intro to Informatics/Projects/Heart-Disease-Dashboard-Streamlit-/data/heart_2022_no_nans.csv")



# Sidebar

stroke_color = st.sidebar.selectbox('Color by', {'HadStroke', 'HadHeartAttack'})

data_sidebar = st.sidebar.selectbox('Select Data', {'State', 'Sex', 'GeneralHealth', 'PhysicalHealthDays',
       'MentalHealthDays', 'LastCheckupTime', 'PhysicalActivities',
       'SleepHours', 'RemovedTeeth', 'HadHeartAttack', 'HadAngina',
       'HadStroke', 'HadAsthma', 'HadSkinCancer', 'HadCOPD',
       'HadDepressiveDisorder', 'HadKidneyDisease', 'HadArthritis',
       'HadDiabetes', 'DeafOrHardOfHearing', 'BlindOrVisionDifficulty',
       'DifficultyConcentrating', 'DifficultyWalking',
       'DifficultyDressingBathing', 'DifficultyErrands', 'SmokerStatus',
       'ECigaretteUsage', 'ChestScan', 'RaceEthnicityCategory', 'AgeCategory',
       'HeightInMeters', 'WeightInKilograms', 'BMI', 'AlcoholDrinkers',
       'HIVTesting', 'FluVaxLast12', 'PneumoVaxEver', 'TetanusLast10Tdap',
       'HighRiskLastYear', 'CovidPos', 'State_ABR'})

data_sidebar_values = st.sidebar.selectbox('Select Value', dat[data_sidebar].unique())

# Graphs

# By Column
hist1 = px.histogram(dat , x = data_sidebar, color = stroke_color)


## Bubble Map
fig = px.scatter_geo(dat,
                     locations= "State_ABR", 
                     locationmode="USA-states",
                     scope="usa")



# Row A
a1, a2 = st.columns((5,5))

with a1:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)




# Row B
# Heat Map
st.markdown('### Map')
st.plotly_chart(fig, use_container_width=True)











