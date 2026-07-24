import streamlit as st
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os


# Page Configuration

st.set_page_config(
    page_title="MediVision AI Pro",
    page_icon="🏥",
    layout="wide"
)


st.title("🏥 MediVision AI Pro")
st.subheader("📄 Patient Medical Report Generator")


# Upload Dataset

uploaded_file = st.file_uploader(
    "📂 Upload Hospital Dataset",
    type=["csv", "xlsx"]
)


if uploaded_file is not None:


    if uploaded_file.name.endswith(".csv"):

        data = pd.read_csv(uploaded_file)

    else:

        data = pd.read_excel(uploaded_file)



    st.success("✅ Dataset Loaded Successfully")


    st.subheader("📋 Dataset Preview")

    st.dataframe(data.head())



    st.write("---")


    # Patient Selection

    st.subheader("👤 Select Patient")


    patient_name = st.selectbox(
        "Choose Patient Name",
        data["Name"]
    )


    patient = data[
        data["Name"] == patient_name
    ].iloc[0]



    patient_id = "MVP-" + str(
        list(data["Name"]).index(patient_name) + 1
    ).zfill(3)



    report_date = datetime.now().strftime(
        "%d-%m-%Y"
    )



    st.success(
        f"Selected Patient : {patient_name}"
    )



    if st.button("📄 Generate Patient Report"):


        os.makedirs(
            "reports",
            exist_ok=True
        )


        file_path = "reports/Patient_Medical_Report.pdf"



        pdf = canvas.Canvas(
            file_path,
            pagesize=letter
        )



        # Logo

        logo_path = "assets/logo.png"


        if os.path.exists(logo_path):

            pdf.drawImage(
                logo_path,
                50,
                710,
                width=70,
                height=70
            )



        # Header

        pdf.setFont(
            "Helvetica-Bold",
            18
        )


        pdf.drawString(
            160,
            750,
            "MediVision AI Pro"
        )


        pdf.setFont(
            "Helvetica",
            12
        )


        pdf.drawString(
            160,
            730,
            "Patient Medical Report"
        )


        pdf.line(
            50,
            700,
            550,
            700
        )



        # Patient ID and Date


        pdf.setFont(
            "Helvetica",
            10
        )


        pdf.drawString(
            70,
            675,
            f"Patient ID : {patient_id}"
        )


        pdf.drawString(
            400,
            675,
            f"Date : {report_date}"
        )



        # Patient Information


        pdf.setFont(
            "Helvetica-Bold",
            14
        )


        pdf.drawString(
            50,
            630,
            "Patient Information"
        )


        pdf.line(
            50,
            620,
            550,
            620
        )


        pdf.setFont(
            "Helvetica",
            12
        )


        pdf.drawString(
            70,
            590,
            f"Name : {patient['Name']}"
        )


        pdf.drawString(
            70,
            570,
            f"Age : {patient['Age']}"
        )


        pdf.drawString(
            70,
            550,
            f"Gender : {patient['Gender']}"
        )


        pdf.drawString(
            70,
            530,
            f"Blood Type : {patient['Blood Type']}"
        )


        # Medical Details


        pdf.setFont(
            "Helvetica-Bold",
            14
        )


        pdf.drawString(
            50,
            490,
            "Medical Details"
        )


        pdf.line(
            50,
            480,
            550,
            480
        )


        pdf.setFont(
            "Helvetica",
            12
        )


        pdf.drawString(
            70,
            450,
            f"Medical Condition : {patient['Medical Condition']}"
        )


        pdf.drawString(
            70,
            430,
            f"Medication : {patient['Medication']}"
        )


        pdf.drawString(
            70,
            410,
            f"Test Result : {patient['Test Results']}"
        )


        pdf.drawString(
            70,
            390,
            f"Admission Type : {patient['Admission Type']}"
        )



        # Hospital Details


        pdf.setFont(
            "Helvetica-Bold",
            14
        )


        pdf.drawString(
            50,
            350,
            "Hospital Details"
        )


        pdf.line(
            50,
            340,
            550,
            340
        )


        pdf.setFont(
            "Helvetica",
            12
        )


        pdf.drawString(
            70,
            310,
            f"Doctor : {patient['Doctor']}"
        )


        pdf.drawString(
            70,
            290,
            f"Hospital : {patient['Hospital']}"
        )


        pdf.drawString(
            70,
            270,
            f"Insurance Provider : {patient['Insurance Provider']}"
        )



        # Billing Information


        pdf.setFont(
            "Helvetica-Bold",
            14
        )


        pdf.drawString(
            50,
            230,
            "Billing Information"
        )


        pdf.line(
            50,
            220,
            550,
            220
        )


        pdf.setFont(
            "Helvetica",
            12
        )


        pdf.drawString(
            70,
            190,
            f"Billing Amount : {patient['Billing Amount']}"
        )



        # AI Analysis


        pdf.setFont(
            "Helvetica-Bold",
            14
        )


        pdf.drawString(
            50,
            150,
            "AI Analysis"
        )


        pdf.line(
            50,
            140,
            550,
            140
        )


        pdf.setFont(
            "Helvetica",
            12
        )


        pdf.drawString(
            70,
            110,
            "System : MediVision AI Pro"
        )


        pdf.drawString(
            70,
            90,
            "Report Status : Generated Successfully"
        )



        # Footer


        pdf.line(
            50,
            60,
            550,
            60
        )


        pdf.setFont(
            "Helvetica",
            10
        )


        pdf.drawString(
            70,
            40,
            "Generated by MediVision AI Pro"
        )


        pdf.drawString(
            350,
            40,
            "Developer : Krishna Ojha"
        )



        # Save PDF


        pdf.save()



        st.success(
            "✅ Patient Medical Report Generated Successfully"
        )


        # Download Button


        with open(
            file_path,
            "rb"
        ) as file:


            st.download_button(

                label="⬇ Download Patient Report",

                data=file,

                file_name="MediVision_Patient_Report.pdf",

                mime="application/pdf"

            )