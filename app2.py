import streamlit as st
from streamlit_extras import add_vertical_space
import streamlit.components.v1 as components
from annotated_text import annotated_text
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objs as go
from src.Predictive_Maintenance.pipelines.prediction_pipeline import prediction

st.set_page_config(layout='wide')

# Custom CSS to further beautify the app
st.markdown("""
    <style>
        /* Change the background color */
        .stApp {
            background-color: #F0F0F0;
        }
        /* Customize sidebar */
        .css-1lcbmhc {
            background-color: #E8E8E8 !important;
        }
        /* Style headings */
        h1 {
            color: #1E90FF;
        }
        h2 {
            color: #1E90FF;
        }
        h3 {
            color: #1E90FF;
        }
        /* Style text */
        .css-1v3fvcr p {
            color: #000000;
        }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("🔧 Predictive Maintenance Project")
    choice = st.radio("Choose from the below options:", ["Main", "EDA", "Monitoring Reports", "Performance Measures", "Prediction"])

if choice == "Main":
    with open("frontend/main/main_page.md", "r") as file:
        readme_contents = file.read()
    st.markdown(readme_contents)

elif choice == "EDA":
    st.title('🔍 Exploratory Data Analysis')

    questions = [
        ("What are the minimum, maximum, and typical values for 'air temperature', 'process temperature', 'rotational speed', 'torque', and 'tool wear'?", "reports/q3.png", "Rotational speed may or may not be actual outliers, therefore we keep them in the dataset for now."),
        ("How is the 'productID' variable distributed across the dataset? Specifically, how many instances correspond to low, medium, and high-quality variants?", "reports/q2.png", "Low quality variant makes up majority of the dataset with 60% of the data, followed by medium quality variant with 30% and high quality variant with 10%"),
        ("What is the frequency distribution of the target label 'machine failure' in the dataset? How many instances indicate a failure compared to those that do not?", "reports/q1.png", "The success rate of the machine is 96.52% and the highest type of failure is HDF (Heat Dissipation Failure) with 1.15% failure rate."),
        ("Is the 'rotational speed' higher for high-quality products than for low-quality products? Is there any correlation of 'productIDs' with other continuous variable?", "reports/q5.png", "Process Temperature seems to have an effect on high quality variant machines. Therefore we can say that Process Temperature is correlated with machine type."),
        ("Is there any correlation between the continuous variables and the 'machine failure' label? For example, does the tool wear increase the likelihood of machine failure?", "reports/q4.png", "Null Hypothesis: There is no significant relationship between the different columns and Machine Failure\nAlternate Hypothesis: There is a significant relationship between the tool wear and the machine failure label", "reports/h0.png"),
        ("Are there any significant interactions or non-linear relationships between the variables that could be important for predictive maintenance? For example, does torque increase non-linearly with rotational speed?", "reports/q6.png", "Among all possible combinations of continuous variables, Rotational Speed vs Torque have a negative correlation and process temperature vs air temperature have a positive correlation."),
        ("Are there any discernible patterns or anomalies in the timing of machine failures? How do machine failure rates change over time?", None, "At present the data does not show recorded time of the failure neither it shows the time of sensor data capture. Hence it is difficult to comment on failure rates over time."),
        ("Are there any notable differences in the distribution of continuous variables between different product types?", "reports/q8.png", "Process Temperature seems to have an effect on high quality variant machines. Therefore we can say that Process Temperature is correlated with machine type."),
        ("How does the occurrence of machine failure vary with different operating conditions, such as air temperature and rotational speed?", "reports/q92.png", "Process Temperature seems to have an effect on high quality variant machines. Therefore we can say that Process Temperature is correlated with machine type.")
    ]

    for idx, (question, img, explanation, *extra_img) in enumerate(questions):
        st.header(f'Question {idx + 1}')
        st.write(question)
        if img:
            st.image(img)
        st.write(f"**{explanation}**")
        if extra_img:
            st.image(extra_img[0])

elif choice == "Performance Measures":
    st.title("📈 Performance Measures")

    models = [
        ("Model 1", "Random Forest Classifier", "reports/model1n.png"),
        ("Model 2", "Random Forest Classifier-registered", "reports/model2n.png")
    ]

    for model_title, model_description, img in models:
        st.title(model_title)
        annotated_text((f"Best {model_title}", model_description))
        st.image(img)

elif choice == "Monitoring Reports":
    st.title("📊 Monitoring Reports")

    options = st.selectbox('Choose the reports:', ('Data Report', 'Model 1 report', 'Model 2 report'))
    
    report_files = {
        'Data Report': "reports/data_drift.html",
        'Model 1 report': "reports/classification_performance_report.html",
        'Model 2 report': "reports/classification_performance_report2.html"
    }
    
    if options in report_files:
        with open(report_files[options], "r", encoding="utf-8") as f:
            html_report = f.read()
        components.html(html_report, scrolling=True, height=700)

elif choice == "Prediction":
    st.title('🔮 Predictive Maintenance')
    st.write("**Please enter the following parameters**")

    col1, col2 = st.columns(2)

    with col1:
        type = st.selectbox('Type', ('Low', 'Medium', 'High'))
        st.write('You selected:', type)
        
        rpm = st.number_input('RPM', value=1500.0)
        st.write('The current rpm is ', rpm)
        
        torque = st.number_input('Torque', value=75)
        st.write('The current torque is ', torque)

    with col2:
        tool_wear = st.number_input('Tool Wear', value=25.00)
        st.write('The current tool wear is ', tool_wear)
        
        air_temp = st.number_input('Air Temperature', value=35.4)
        st.write('The current air temperature is ', air_temp)
        
        process_temp = st.number_input('Process Temperature', value=46.65)
        st.write('The current process temperature is ', process_temp)
    
    if st.button("Predict"):
        result1, result2 = prediction(type, rpm, torque, tool_wear, air_temp, process_temp)
        st.write("Machine Failure?: ", result1)
        st.write("Type of Failure: ", result2)
