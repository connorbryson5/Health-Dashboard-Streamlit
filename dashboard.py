# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 14:07:21 2023

@author: Connor Bryson
"""

# Libraries

import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_antd_components as sac

# Page Layout

st.set_page_config(layout = "wide", initial_sidebar_state= "expanded")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html = True)


## Sidebar
st.sidebar.header('Indicators of Heart Disease Dashboard')



# Caching data
@st.cache_data
def get_data(filename):
    dat = pd.read_csv(filename, index_col = False)
    return dat

# Data (Laptop)
## dat = get_data("C:/Users/Connor/Desktop/Intro to Informatics/Projects/Heart-Disease-Dashboard-Streamlit-/data/heart_2022_no_nans.csv")
# Data (Desktop )
dat = get_data("C:/Users/cdbry/Desktop/Info501/Heart-Disease-Dashboard-Streamlit-/data/heart_2022_no_nans.csv")

dat.State.unique()
# Sidebar

with st.sidebar:
    st.sidebar.subheader('Select Data')
    state_checkbox = sac.tree(items=[
        
        # State
        sac.TreeItem('State', children=[
            sac.TreeItem('Alabama'), 
            sac.TreeItem('Alaska'),
            sac.TreeItem('Arizona'),
            sac.TreeItem('Arkansas'),
            sac.TreeItem('California'),
            sac.TreeItem('Colorado'),
            sac.TreeItem('Connecticut'),
            sac.TreeItem('Delaware'),
            sac.TreeItem('District of Columbia'),
            sac.TreeItem('Florida'),
            sac.TreeItem('Georgia'),
            sac.TreeItem('Hawaii'), 
            sac.TreeItem('Idaho'),
            sac.TreeItem('Illinois'),
            sac.TreeItem('Indiana'),
            sac.TreeItem('Iowa'), 
            sac.TreeItem('Kansas'),
            sac.TreeItem('Kentucky'),
            sac.TreeItem('Louisiana'),
            sac.TreeItem('Maine'),
            sac.TreeItem('Maryland'),
            sac.TreeItem('Massachusetts'),
            sac.TreeItem('Michigan'),
            sac.TreeItem('Minnesota'),
            sac.TreeItem('Mississippi'),
            sac.TreeItem('Missouri'),
            sac.TreeItem('Montana'),
            sac.TreeItem('Nebraska'),
            sac.TreeItem('Nevada'),
            sac.TreeItem('New Hampshire'),
            sac.TreeItem('New Jersey'),
            sac.TreeItem('New Mexico'),
            sac.TreeItem('New York'),
            sac.TreeItem('North Carolina'),
            sac.TreeItem('North Dakota'),
            sac.TreeItem('Ohio'),
            sac.TreeItem('Oklahoma'),
            sac.TreeItem('Oregon'),
            sac.TreeItem('Pennsylvania'),
            sac.TreeItem('Rhode Island'),
            sac.TreeItem('South Carolina'), 
            sac.TreeItem('South Dakota'),
            sac.TreeItem('Tennessee'),
            sac.TreeItem('Texas'),
            sac.TreeItem('Utah'), 
            sac.TreeItem('Vermont'),
            sac.TreeItem('Virginia'),
            sac.TreeItem('Washington'),
            sac.TreeItem('West Virginia'),
            sac.TreeItem('Wisconsin'),
            sac.TreeItem('Wyoming'),
            sac.TreeItem('Guam'),
            sac.TreeItem('Puerto Rico'),
            sac.TreeItem('Virgin Islands')
            ]),
        
        ], index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
        format_func='title', icon='table', open_all=False, checkbox=True)
    
        # Age 
    age_group_checkbox = sac.tree(items=[
        sac.TreeItem('Age Group', children=[
            sac.TreeItem('Age 18 to 24'), 
            sac.TreeItem('Age 25 to 29'),
            sac.TreeItem('Age 30 to 34'),
            sac.TreeItem('Age 35 to 39'),
            sac.TreeItem('Age 40 to 44'),
            sac.TreeItem('Age 45 to 49'),
            sac.TreeItem('Age 50 to 54'),
            sac.TreeItem('Age 55 to 59'),
            sac.TreeItem('Age 60 to 64'),
            sac.TreeItem('Age 65 to 69'),
            sac.TreeItem('Age 70 to 74'),
            sac.TreeItem('Age 75 to 79'),
            sac.TreeItem('Age 80 or older')]),
        
        ], index=[1,2,3,4,5,6,7,8,9,10,11,12,13], format_func='title', icon='table', open_all=False, checkbox=True)
        
    
        # Sex
    sex_checkbox = sac.tree(items=[
            sac.TreeItem('Sex', children=[
                sac.TreeItem('Male'),
                sac.TreeItem('Female')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
        
        
        # Race/Ethnicity
    race_ethnicity_checkbox = sac.tree(items=[
     sac.TreeItem('Race/Etnicity', children=[
         sac.TreeItem('White only, Non-Hispanic'), 
         sac.TreeItem('Black only, Non-Hispanic'),
         sac.TreeItem('Other race only, Non-Hispanic'),
         sac.TreeItem('Multiracial, Non-Hispanic'),
         sac.TreeItem('Hispanic'),
         ]),
     ], index = [1,2,3,4,5], format_func='title', icon='table', open_all=False, checkbox=True)   
    
    
        # General Health
    general_health_checkbox = sac.tree(items=[
        sac.TreeItem('General Health', children=[
            sac.TreeItem('Poor'), 
            sac.TreeItem('Fair'),
            sac.TreeItem('Good'),
            sac.TreeItem('Very good'),
            sac.TreeItem('Excellent'),
            ]),
        ], index = [1,2,3,4,5], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Last Checkup Time
    last_checkup_time_checkbox = sac.tree(items=[
            sac.TreeItem('Last Checkup Time', children=[
                sac.TreeItem('Within past year (anytime less than 12 months ago)'),
                sac.TreeItem('Within past 2 years (1 year but less than 2 years ago)'),
                sac.TreeItem('Within past 5 years (2 years but less than 5 years ago)'),
                sac.TreeItem( '5 or more years ago')]),
            ], index = [1,2,3,4], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Smoker Status
    smoker_status_checkbox = sac.tree(items=[
        sac.TreeItem('Smoker Status', children=[
            sac.TreeItem('Never smoked'), 
            sac.TreeItem('Former smoker'),
            sac.TreeItem('Current smoker - now smokes some days'),
            sac.TreeItem('Current smoker - now smokes every day')]),
        ], index = [1,2,3,4], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
    
        # E-Cigarrette
    ecigarrette_checkbox = sac.tree(items=[
            sac.TreeItem('E-Cigarette Usage', children=[
                sac.TreeItem('Never used e-cigarettes in my entire life'), 
                sac.TreeItem('Not at all (right now)'),
                sac.TreeItem( 'Use them some days'),
                sac.TreeItem('Use them every day')]),
            ], index = [1,2,3,4], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Removed Teeth
    removed_teeth_checkbox = sac.tree(items=[
            sac.TreeItem('Number of Teeth Removed', children=[
                sac.TreeItem('None of them'), 
                sac.TreeItem('1 to 5'),
                sac.TreeItem('6 or more, but not all'),
                sac.TreeItem('All')]),
            ], index = [1,2,3,4], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
    
        # Have Recieved Tetanus or Tdap in last 10 Years
    removed_teeth_checkbox = sac.tree(items=[
        sac.TreeItem('Recieved Tetanus or Tdap in last 10 Years', children=[
            sac.TreeItem('No, did not receive any tetanus shot in the past 10 years'), 
            sac.TreeItem('Yes, received Tdap'),
            sac.TreeItem('Yes, received tetanus shot but not sure what type'),
            sac.TreeItem('Yes, received tetanus shot, but not Tdap')]),
        ], index = [1,2,3,4], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    st.dataframe(general_health_checkbox)   
        



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



stroke_color = st.sidebar.selectbox('Color by', {'State', 'Sex', 'GeneralHealth', 'PhysicalHealthDays',
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

# Graphs

# Histogram
hist1 = px.histogram(dat , x = data_sidebar, color = stroke_color, barmode='group', text_auto=True,
                     title= f"{data_sidebar} Data broken down by {stroke_color}")

# Boxplot
boxplot1 = px.box(dat, y=data_sidebar)



## Bubble Map
map1 = px.scatter_geo(dat,
                     locations= dat[dat[data_sidebar] == data_sidebar_values].value_counts(subset = ["State_ABR"], sort = False).reset_index().State_ABR, 
                     locationmode="USA-states",
                     size = dat[dat[data_sidebar] == data_sidebar_values].value_counts(subset = ["State_ABR"], sort = False),
                     scope="usa")




st.markdown('# Indicators of Heart Disease')



# Row A

b1, b2 = st.columns((3,7))


with b1:
    st.markdown('### Boxplot chart')
    st.plotly_chart(boxplot1, use_container_width=True)


with b2:
    st.markdown('### Bar chart')
    st.plotly_chart(hist1, use_container_width=True)



# Row B
st.markdown('### Map')

b1, b2 = st.columns((2,8))

# Heat Map


with b1: 
    df = dat[dat[data_sidebar] == data_sidebar_values].value_counts(subset = ["State_ABR", "State"], sort = False).to_frame('Count').reset_index()
    st.dataframe(df, 
                 hide_index = True,
                 use_container_width=True, 
                 column_config={
                "State_ABR": None
                })
    
    
with b2:
    
     st.plotly_chart(map1, use_container_width=True)



st.dataframe(dat[dat[data_sidebar] == data_sidebar_values])







