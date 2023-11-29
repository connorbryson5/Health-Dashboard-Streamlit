
# Streamlit Health Dashboard (United States) 

Stremlit Link for Dashboard: https://health-dashboard-united-states-2022.streamlit.app/


## Abstract

The original goal of this project was to create a dashboard that allows users to
understand trends within the data and derive insights into which factors have a larger
affect on heart disease. 

As I worked on the project, I realized that the data that I was using was not very well suited to predict Heart Disease. However, with so many variables I decided that it would be best to turn this dashboard into an interactive dashboard that allows you to see how many people have specific conditions and how it compares to other groups. I created a map that allows you to see the breakdown of people in each state by the specifications that you choose.

**Disclaimer:** My hope is that users will be able to reflect on each of the factors for their own
health. However, this dashboard is not meant to replace seeing a doctor if someone is
dealing with health problems. The inferences that can be made with this dashbaord should be used knowing that the results are just for this survey of people when the survey was taken.

Overall this project was really fun to work on, and I hope you enjoy messing around with it. Any specific question you can think of try to see if you can do it with the data.



## The Data


The data comes from the [Indicators of Heart Disease (2022 UPDATE)](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease) dataset by Kaggle User "Kamil Pytlake".

In his description he states that,
"The dataset originally comes from the CDC and is a major part of the Behavioral Risk Factor Surveillance System (BRFSS), which conducts annual telephone surveys to collect data on the health status of U.S. residents." This data also was only for the year 2022. 

The dataset has been reduced to 40 variables as the original dataset was over 300 variables. I also created a new "State_ABR" column that has all of the State and Territory 2 Letter Abreviations. This was to work with the plotly bubble size map.

Here is a link to the [variable documentation](https://github.com/kamilpytlak/data-science-projects/blob/main/heart-disease-prediction/2022/documentation/vars_list_with_descriptions.txt) if you would like to see how the survey was phrased to participants.

Finally, if you're curious where the raw data came from click [here](https://www.cdc.gov/brfss/annual_data/annual_2022.html)


## Algorithms

Since this dashboard is a visual dashbaord, there is only 1 custom algorithm used which is called "get_data()". This function allows me to cache the data through streamlit to help make the app run faster. There are no machine learning algorithms in this dashboard.

Otherwise for all of the visualizations please refer to the plotly python package documentation linked here:  
https://plotly.github.io/plotly.py-docs/generated/plotly.html

If you want all of the types of graphs you can make in python with plotly 
click here:  
https://plotly.com/python/
## Acknowledgements

Once again, big thank you to [Kamil Pytlak](https://www.kaggle.com/kamilpytlak) for the data and the inspriration to build this dashboard.

Also huge thanks to Github User [nicedouble](https://github.com/nicedouble) for the [StreamlitAntdComponents](https://github.com/nicedouble/StreamlitAntdComponents) package which allowed me to do the custom checkboxes found in the sidebar of the app.


## Tools Used

**Programming Language:**  *Python*

**Packages Used**:  

    Streamlit - For customization of the app itself including the sidebar, header, selectboxes, sliders, and positioning of the elements in the app.  

    Pandas - For filtering the data, loading in the data, and creation of new data frames.  

    PlotlyExpress-  For all of the custom graphs and visualizations.   

    streamlit_antd_components- For the custom checkboxes on the sidebar to select your data.

**App Hosting:**   

    Github - Repository where you are right now and for all of my code, screenshots, etc.

**App Deployment:** 
    
    Streamlit - App Deployment site for public hosting. Full integration with python code.

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/connorbryson5/Heart-Disease-Dashboard-Streamlit-/main/screenshots/Screenshot1.JPG)

![App Screenshot](https://raw.githubusercontent.com/connorbryson5/Heart-Disease-Dashboard-Streamlit-/main/screenshots/Screenshot2.JPG)

![App Screenshot](https://raw.githubusercontent.com/connorbryson5/Heart-Disease-Dashboard-Streamlit-/main/screenshots/Screenshot3.JPG)

![App Screenshot](https://raw.githubusercontent.com/connorbryson5/Heart-Disease-Dashboard-Streamlit-/main/screenshots/Screenshot4.JPG)