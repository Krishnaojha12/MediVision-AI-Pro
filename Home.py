import streamlit as st
import time


# Page Configuration
st.set_page_config(
    page_title="MediVision AI Pro",
    page_icon="🏥",
    layout="wide"
)
#SIDEBAR 
with st.sidebar:

    st.title("🏥 MediVision AI Pro")

    st.markdown("---")

    st.subheader("📌 Navigation") 

    if st.button("🏠 Home", use_container_width=True):
        st.rerun()


    if st.button("📂 Upload Dataset", use_container_width=True):
        st.switch_page("pages/1_Data_Upload.py")


    if st.button("🧹 Data Cleaning", use_container_width=True):
        st.switch_page("pages/2_Data_Cleaning.py")


    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("pages/3_Dashboard.py")


    if st.button("🤖 AI Assistant", use_container_width=True):
        st.switch_page("pages/4_AI_Assistant.py")


    if st.button("🧠 Machine Learning", use_container_width=True):
        st.switch_page("pages/5_Machine_Learning.py")


    if st.button("📄 PDF Report", use_container_width=True):
        st.switch_page("pages/6_Report.py")


    st.markdown("---")

    st.caption("Version 1.0")
    st.caption("Developed by Krishna Ojha")



# HOME PAGE
st.title("🏥 MediVision AI Pro")


st.subheader(
    "AI Powered Healthcare Data Analytics Platform"
)



st.write(
"""
Welcome to **MediVision AI Pro** 🚀

An intelligent healthcare analytics platform designed for:

✅ Hospital Dataset Management

✅ Data Cleaning & Preprocessing

✅ Interactive Data Visualization

✅ AI Based Healthcare Insights

✅ Machine Learning Prediction

✅ Automated PDF Reports

"""
)



st.info(
"🚀 Select any module from the sidebar to start analysis."
)



st.divider()



#PROJECT OVERVIEW 


st.subheader("📊 Project Overview")


col1, col2, col3, col4 = st.columns(4)



with col1:
    st.metric(
        "📂 Modules",
        "6"
    )


with col2:
    st.metric(
        "🤖 AI System",
        "Enabled"
    )


with col3:
    st.metric(
        "🧠 ML Model",
        "Ready"
    )


with col4:
    st.metric(
        "📄 Reports",
        "PDF"
    )



st.divider()



# Loading Animation

with st.spinner("🚀 Initializing MediVision AI Pro..."):
    time.sleep(1)



st.success(
"✅ Application Ready Successfully"
)



#FEATURES
st.header("🚀 Project Features")
col1, col2, col3 = st.columns(3)
with col1:

    st.info(
"""
📊 Dashboard

15+ Interactive Charts
"""
)

with col2:

    st.success(
"""
🤖 AI Assistant

Smart Healthcare Insights
"""
)

with col3:

    st.warning(
"""
📄 Reports

PDF + Excel Generation
"""
)



st.divider()

st.header("🎯 Project Goal")

st.write(
"""
The main goal of MediVision AI Pro is to provide an intelligent
healthcare analytics system that helps in:

✅ Managing hospital datasets

✅ Finding useful healthcare insights

✅ Supporting decision making using AI and Machine Learning

"""
)

st.header("📖 About MediVision AI Pro")

st.write(
"""
**MediVision AI Pro** is an AI-powered healthcare analytics application.

It helps hospitals and healthcare professionals to:

✅ Upload and manage patient datasets

✅ Clean and preprocess healthcare records

✅ Analyze data using visualization

✅ Predict Breast Cancer using Machine Learning

✅ Generate professional reports

The main goal of this project is to make healthcare data analysis
simple, efficient and user-friendly.
"""
)
st.divider()

st.header("📌 Modules Included")

st.markdown(
"""
- 📂 Dataset Upload
- 🧹 Data Cleaning
- 📊 Interactive Dashboard
- 🤖 AI Assistant
- 🧠 Machine Learning
- 📄 PDF Report Generation
"""
)
st.divider()

st.header("🛠 Technology Stack")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "🐍 Language",
        "Python"
    )


with col2:
    st.metric(
        "🎈 Framework",
        "Streamlit"
    )


with col3:
    st.metric(
        "🧠 Machine Learing",
        "Random Forest"
    )


with col4:
    st.metric(
        "📊 Analytics",
        "Healthcare Analytics"
    )

st.divider()

st.header("👨‍💻 Developer")

st.write(
"""
**MediVision AI Pro**

Developed by: Team

Purpose:
Healthcare Data Analytics Project using Python,
Streamlit, Machine Learning and Artificial Intelligence.
"""
)