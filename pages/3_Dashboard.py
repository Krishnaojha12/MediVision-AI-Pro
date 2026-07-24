import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 MediVision AI Pro Dashboard")

uploaded_file = st.file_uploader(
    "📂 Upload Hospital Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.success("Dataset Uploaded Successfully ✅")

    st.write("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Total Patients", len(data))

    with col2:
        st.metric("👨 Male Patients", (data["Gender"] == "Male").sum())

    with col3:
        st.metric("👩 Female Patients", (data["Gender"] == "Female").sum())

    with col4:
        st.metric("🏥 Total Hospitals", data["Hospital"].nunique())

    st.write("---")

    col5, col6 = st.columns(2)

    with col5:
        st.metric("🎂 Average Age", round(data["Age"].mean(), 2))

    with col6:
        st.metric("💰 Average Billing", f"${round(data['Billing Amount'].mean(),2)}")

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👨 Gender Distribution")

    gender_count = data["Gender"].value_counts()

    gender_chart = px.bar(
        x=gender_count.index,
        y=gender_count.values,
        labels={
            "x": "Gender",
            "y": "Patients"
        },
        title="Male vs Female Patients"
    )

    st.plotly_chart(gender_chart, use_container_width=True)

    with col2:
        st.subheader("🩺 Disease Distribution")

    disease_count = data["Medical Condition"].value_counts()

    disease_chart = px.pie(
        names=disease_count.index,
        values=disease_count.values,
        title="Medical Conditions"
    )

    st.plotly_chart(disease_chart, use_container_width=True)

    st.write("---")

    st.subheader("📊 Age Distribution")

    age_chart = px.histogram(
        data,
        x="Age",
        nbins=10,
        title="Patient Age Distribution"
)

    st.plotly_chart(age_chart, use_container_width=True)


    st.write("---")

    st.subheader("📈 Billing Amount Distribution")

    histogram = px.histogram(
        data,
        x="Billing Amount",
        nbins=20,
        title="Billing Amount Histogram"
)

    st.plotly_chart(histogram, use_container_width=True)

    st.write("---")

    st.subheader("💉 Admission Type Distribution")

    admission_count = data["Admission Type"].value_counts()

    admission_chart = px.pie(
        names=admission_count.index,
        values=admission_count.values,
        title="Admission Type"
)

    st.plotly_chart(admission_chart, use_container_width=True)

    st.success("🎉 Dashboard Loaded Successfully")