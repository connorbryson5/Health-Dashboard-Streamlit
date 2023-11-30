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



# Caching data
@st.cache_data
def get_data(filename):
    dat = pd.read_csv(filename, index_col = False)
    return dat


dat = get_data("https://github.com/connorbryson5/Health-Dashboard-Streamlit/blob/main/data/heart_2022_no_nans.csv?raw=True")







# Sidebar



with st.sidebar:
    
    st.sidebar.header('Health Dashboard (United States)')
    
    st.sidebar.subheader('Created by Connor Bryson')
    
    st.sidebar.markdown('---')
    
    
    
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
        
        ], index=[1,2,3,4,5,6,7,8,9,10,11,12,13], icon='table', open_all=False, checkbox=True)
        
    
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
     ], index = [1,2,3,4,5], icon='table', open_all=False, checkbox=True)   
    
    
        # General Health
    general_health_checkbox = sac.tree(items=[
        sac.TreeItem('General Health', children=[
            sac.TreeItem('Poor'), 
            sac.TreeItem('Fair'),
            sac.TreeItem('Good'),
            sac.TreeItem('Very good'),
            sac.TreeItem('Excellent'),
            ]),
        ], index = [1,2,3,4,5], icon='table', open_all=False, checkbox=True)
    
    
        # Last Checkup Time
    last_checkup_time_checkbox = sac.tree(items=[
            sac.TreeItem('Last Checkup Time', children=[
                sac.TreeItem('Within past year (anytime less than 12 months ago)'),
                sac.TreeItem('Within past 2 years (1 year but less than 2 years ago)'),
                sac.TreeItem('Within past 5 years (2 years but less than 5 years ago)'),
                sac.TreeItem( '5 or more years ago')]),
            ], index = [1,2,3,4], icon='table', open_all=False, checkbox=True)
    
    
        # Had Chest Scan
    chest_scan_checkbox = sac.tree(items=[
            sac.TreeItem('Had Chest Scan', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Drink Alcohol
    alcohol_checkbox = sac.tree(items=[
            sac.TreeItem('Drink Alcohol', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Smoker Status
    smoker_status_checkbox = sac.tree(items=[
        sac.TreeItem('Smoker Status', children=[
            sac.TreeItem('Never smoked'), 
            sac.TreeItem('Former smoker'),
            sac.TreeItem('Current smoker - now smokes some days'),
            sac.TreeItem('Current smoker - now smokes every day')]),
        ], index = [1,2,3,4], icon='table', open_all=False, checkbox=True)
    
    
    
        # E-Cigarrette
    ecigarrette_checkbox = sac.tree(items=[
            sac.TreeItem('E-Cigarette Usage', children=[
                sac.TreeItem('Never used e-cigarettes in my entire life'), 
                sac.TreeItem('Not at all (right now)'),
                sac.TreeItem( 'Use them some days'),
                sac.TreeItem('Use them every day')]),
            ], index = [1,2,3,4], icon='table', open_all=False, checkbox=True)
    
    
        # Removed Teeth
    removed_teeth_checkbox = sac.tree(items=[
            sac.TreeItem('Number of Teeth Removed', children=[
                sac.TreeItem('None of them'), 
                sac.TreeItem('1 to 5'),
                sac.TreeItem('6 or more, but not all'),
                sac.TreeItem('All')]),
            ], index = [1,2,3,4], icon='table', open_all=False, checkbox=True)
    
        
    
        # Tested Positive for COVID-19
    covid_checkbox = sac.tree(items=[
            sac.TreeItem('Ever Tested Positive for COVID-19', children=[
                sac.TreeItem('No'),
                sac.TreeItem('Yes'),
                sac.TreeItem('Tested positive using home test without a health professional')]),
            ], index = [1,2,3], icon='table', open_all=False, checkbox=True)
    
    
        # Tested for HIV
    hiv_checkbox = sac.tree(items=[
            sac.TreeItem('Tested for HIV', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], icon='table', open_all=False, checkbox=True)
    
    
        # Have Recieved Flu Shot in last 12 Months
    flu_checkbox = sac.tree(items=[
            sac.TreeItem('Recieved Flu Shot in last 12 Months', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Have Ever Recieved Pneumonia Shot
    pneumo_checkbox = sac.tree(items=[
            sac.TreeItem('Recieved Pneumonia Shot', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Have Recieved Tetanus or Tdap in last 10 Years
    tetanus_tdap_checkbox = sac.tree(items=[
        sac.TreeItem('Recieved Tetanus or Tdap Shot in last 10 Years', children=[
            sac.TreeItem('No, did not receive any tetanus shot in the past 10 years'), 
            sac.TreeItem('Yes, received Tdap'),
            sac.TreeItem('Yes, received tetanus shot but not sure what type'),
            sac.TreeItem('Yes, received tetanus shot, but not Tdap')]),
        ], index = [1,2,3,4], icon='table', open_all=False, checkbox=True)
    
    
        # Had Diabetes
    diabetes_checkbox = sac.tree(items=[
            sac.TreeItem('Had Diabetes', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('Yes, but only during pregnancy (female)'),
                sac.TreeItem('No'),
                sac.TreeItem('No, pre-diabetes or borderline diabetes')])
            ], index = [1,2,3,4], icon='table', open_all=False, checkbox=True)
    
    
        # Pysically Active
    physically_active_checkbox = sac.tree(items=[
            sac.TreeItem('Physically Active', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Had Heart Attack
    heart_attack_checkbox = sac.tree(items=[
            sac.TreeItem('Had Heart Attack', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Had Angina
    angina_checkbox = sac.tree(items=[
            sac.TreeItem('Had Angina', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
        
        # Had Stroke
    stroke_checkbox = sac.tree(items=[
            sac.TreeItem('Had Stroke', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Had Asthma
    asthma_checkbox = sac.tree(items=[
            sac.TreeItem('Had Asthma', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Had Skin Cancer
    skin_cancer_checkbox = sac.tree(items=[
        sac.TreeItem('Had Skin Cancer', children=[
            sac.TreeItem('Yes'),
            sac.TreeItem('No')]),
        ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
    
        # Had COPD
    copd_checkbox = sac.tree(items=[
            sac.TreeItem('Had Chronic Obstructve Pulmonary Disease (COPD)', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], icon='table', open_all=False, checkbox=True)
    
    
        # Had Depressive Disorder
    depressive_checkbox = sac.tree(items=[
            sac.TreeItem('Had Depressive Disorder', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Had Kidney Disease
    kidney_checkbox = sac.tree(items=[
            sac.TreeItem('Had Kidney Disease', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Had Arthiritis
    arthiritis_checkbox = sac.tree(items=[
            sac.TreeItem('Had Arthritis', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Deaf or Hard of Hearing
    deaf_checkbox = sac.tree(items=[
            sac.TreeItem('Deaf or Hard of Hearing', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Blind or Vision Difficulty
    blind_checkbox = sac.tree(items=[
            sac.TreeItem('Blind or Vision Difficulty', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
    
        # Difficulty Concentrating
    concentration_checkbox = sac.tree(items=[
            sac.TreeItem('Difficulty Concentrating', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
    
        # Difficulty Walking
    walking_checkbox = sac.tree(items=[
            sac.TreeItem('Difficulty Walking', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Difficulty Dressing or Bathing
    bathing_checkbox = sac.tree(items=[
            sac.TreeItem('Difficulty Dressing or Bathing', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Difficulty Doing Errands
    errands_checkbox = sac.tree(items=[
            sac.TreeItem('Difficulty Doing Errands', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
    
    
        # Taken Any Injections or Treated for STD in the Past Year
    high_risk_checkbox = sac.tree(items=[
            sac.TreeItem('Taken Any Injections or Treated for STD in the Past Year', children=[
                sac.TreeItem('Yes'),
                sac.TreeItem('No')]),
            ], index = [1,2], format_func='title', icon='table', open_all=False, checkbox=True)
        
    
    
    
    height_slider = st.select_slider('Height (Meters)', options = sorted(dat.HeightInMeters.unique()),
                                  value = (min(sorted(dat.HeightInMeters.unique())), max(sorted(dat.HeightInMeters.unique()))))
    
    
    weight_slider = st.select_slider('Weight (Kilograms)', options = sorted(dat.WeightInKilograms.unique()),
                                  value = (min(sorted(dat.WeightInKilograms.unique())), max(sorted(dat.WeightInKilograms.unique()))))
    
    
    bmi_slider = st.select_slider('BMI', options = sorted(dat.BMI.unique()),
                                  value = (min(sorted(dat.BMI.unique())), max(sorted(dat.BMI.unique()))))
    
    
    sleep_hours_slider = st.select_slider('Hours of Sleep Per Night', options = sorted(dat.SleepHours.unique()),
                                  value = (min(sorted(dat.SleepHours.unique())), max(sorted(dat.SleepHours.unique()))))
    
    
    physical_health_days_slider = st.select_slider('Number of Days in Poor Physical Health (Last 30 Days)', options = sorted(dat.PhysicalHealthDays.unique()),
                                  value = (min(sorted(dat.PhysicalHealthDays.unique())), max(sorted(dat.PhysicalHealthDays.unique()))))
    
    
    mental_health_days_slider = st.select_slider('Number of Days in Poor Mental Health (Last 30 Days)', options = sorted(dat.MentalHealthDays.unique()),
                                  value = (min(sorted(dat.MentalHealthDays.unique())), max(sorted(dat.MentalHealthDays.unique()))))
    
    
    
    
    
    
    dat1 = dat[dat['State'].isin(state_checkbox) &
               dat['Sex'].isin(sex_checkbox) & 
               dat['GeneralHealth'].isin(general_health_checkbox) &
               dat['PhysicalHealthDays'].between(physical_health_days_slider[0], physical_health_days_slider[1]) &
               dat['MentalHealthDays'].between(mental_health_days_slider[0], mental_health_days_slider[1]) &
               dat['LastCheckupTime'].isin(last_checkup_time_checkbox) &
               dat['PhysicalActivities'].isin(physically_active_checkbox) &
               dat['SleepHours'].between(sleep_hours_slider[0], sleep_hours_slider[1])  &
               dat['RemovedTeeth'].isin(removed_teeth_checkbox) & 
               dat['HadHeartAttack'].isin(heart_attack_checkbox) &
               dat['HadAngina'].isin(angina_checkbox) &
               dat['HadStroke'].isin(stroke_checkbox) &
               dat['HadAsthma'].isin(asthma_checkbox) &
               dat['HadSkinCancer'].isin(skin_cancer_checkbox) &
               dat['HadCOPD'].isin(copd_checkbox) &
               dat['HadDepressiveDisorder'].isin(depressive_checkbox) & 
               dat['HadKidneyDisease'].isin(kidney_checkbox) &
               dat['HadArthritis'].isin(arthiritis_checkbox) &
               dat['HadDiabetes'].isin(diabetes_checkbox) & 
               dat['DeafOrHardOfHearing'].isin(deaf_checkbox) &
               dat['BlindOrVisionDifficulty'].isin(blind_checkbox) &
               dat['DifficultyConcentrating'].isin(concentration_checkbox) &
               dat['DifficultyWalking'].isin(walking_checkbox) &
               dat['DifficultyDressingBathing'].isin(bathing_checkbox) &
               dat['DifficultyErrands'].isin(errands_checkbox) &
               dat['SmokerStatus'].isin(smoker_status_checkbox) &
               dat['ECigaretteUsage'].isin(ecigarrette_checkbox) &
               dat['ChestScan'].isin(chest_scan_checkbox) &
               dat['RaceEthnicityCategory'].isin(race_ethnicity_checkbox) &
               dat['AgeCategory'].isin(age_group_checkbox) &
               dat['HeightInMeters'].between(height_slider[0], height_slider[1]) &
               dat['WeightInKilograms'].between(weight_slider[0], weight_slider[1]) &
               dat['BMI'].between(bmi_slider[0], bmi_slider[1])  &
               dat['AlcoholDrinkers'].isin(alcohol_checkbox) &
               dat['HIVTesting'].isin(hiv_checkbox)  &
               dat['FluVaxLast12'].isin(flu_checkbox) &
               dat['PneumoVaxEver'].isin(pneumo_checkbox) &
               dat['TetanusLast10Tdap'].isin(tetanus_tdap_checkbox) &
               dat['HighRiskLastYear'].isin(high_risk_checkbox) & 
               dat['CovidPos'].isin(covid_checkbox) 
               ]
            




# Main Page 
    
    
    
st.markdown('# Health Dashboard (United States)')





# Row A

a1, a2 = st.columns((3,7))


with a1:
    st.markdown('### Bar chart')
    
    
    histogram_selection1 = st.selectbox('Select Data', {'Sex', 'State', 'GeneralHealth', 'PhysicalHealthDays',
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
    
    histogram_selection2 = st.selectbox('Color by', {'State', 'Sex', 'GeneralHealth', 'PhysicalHealthDays',
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
           'HighRiskLastYear', 'CovidPos', 'State_ABR'}, index = None)
    
    
    histogram_selection3 = st.selectbox('Facet by', {'State', 'Sex', 'GeneralHealth', 'PhysicalHealthDays',
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
           'HighRiskLastYear', 'CovidPos', 'State_ABR'}, index = None)
    

with a2:    
    # Histogram
    hist1 = px.histogram(dat1 , x = histogram_selection1, color = histogram_selection2, barmode='group', text_auto=True,
                         title= f"{histogram_selection1} Data broken down by {histogram_selection2}",
                         facet_col = histogram_selection3)

    
    st.plotly_chart(hist1, use_container_width=True)




st.markdown('### Boxplot chart')

boxplot_columns = st.selectbox('Select Column', {'PhysicalHealthDays',
       'MentalHealthDays', 'SleepHours', 'HeightInMeters', 'WeightInKilograms', 'BMI'})

# Boxplot
boxplot1 = px.box(dat1, y=boxplot_columns)

st.plotly_chart(boxplot1, use_container_width=True)






# Row B
st.markdown('### Map')

b1, b2 = st.columns((2,8))

# Heat Map


with b1: 
    df = dat1.value_counts(subset = ["State_ABR", "State"], sort = False).to_frame('Count').reset_index()
    st.dataframe(df, 
                 hide_index = True,
                 use_container_width=True, 
                 column_config={
                "State_ABR": None
                })
    
    
with b2:
    
    ## Bubble Map
    states = dat1.value_counts(subset = ["State_ABR"], sort = False).to_frame('Count').reset_index().State_ABR
    sizes = dat1.value_counts(subset = ["State_ABR"], sort = False).to_frame('Count').reset_index().Count
    map1 = px.scatter_geo(dat1, locations= states, locationmode="USA-states", size = sizes , scope="usa")
    
    st.plotly_chart(map1, use_container_width=True)




st.dataframe(dat1, use_container_width=True)






