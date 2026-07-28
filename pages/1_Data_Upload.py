import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Dataset Upload",
    page_icon="📂",
    layout="wide"
)


# Session State for Dataset

if "dataset" not in st.session_state:
    st.session_state.dataset = None

st.title("📂 Hospital Dataset Upload")

st.write("Upload your Hospital CSV or Excel Dataset")

st.write("---")


uploaded_file = st.file_uploader(
    "Choose CSV or Excel File",
    type=["csv", "xlsx"]
)



if uploaded_file is not None:

    try:

        # Read CSV File

        if uploaded_file.name.endswith(".csv"):

            data = pd.read_csv(uploaded_file)


        # Read Excel File

        else:

            data = pd.read_excel(uploaded_file)



        # Empty Dataset Check

        if data.empty:

            st.error("❌ Uploaded Dataset is Empty")

            st.stop()



    except Exception as e:

        st.error(
            f"❌ Invalid Dataset or File Format: {e}"
        )

        st.stop()



    # Save Dataset for Other Modules

    st.session_state.dataset = data



    st.success(
        "✅ Dataset Uploaded and Saved Successfully"
    )



    st.write("---")


    # Dataset Preview

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        data,
        use_container_width=True
    )



    # Dataset Information

    rows, cols = data.shape


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Total Rows",
            rows
        )


    with col2:

        st.metric(
            "Total Columns",
            cols
        )


    with col3:

        st.metric(
            "Missing Values",
            data.isnull().sum().sum()
        )



    st.write("---")



    # Column Names

    st.subheader("📝 Column Names")

    st.write(
        list(data.columns)
    )



    # First 5 Rows

    st.subheader("🔝 First 5 Rows")

    st.dataframe(
        data.head()
    )



    # Last 5 Rows

    st.subheader("🔚 Last 5 Rows")

    st.dataframe(
        data.tail()
    )



    # Dataset Shape

    st.subheader("📊 Dataset Shape")

    st.write(
        f"Rows : {data.shape[0]}"
    )

    st.write(
        f"Columns : {data.shape[1]}"
    )



    # Data Types

    st.subheader("📑 Data Types")


    datatype_df = pd.DataFrame(
        {
            "Column Name": data.columns,
            "Data Type": data.dtypes.astype(str)
        }
    )


    st.dataframe(
        datatype_df,
        use_container_width=True
    )



    # Missing Values Analysis

    st.subheader("❓ Missing Values")


    missing_values = pd.DataFrame(
        {
            "Column Name": data.columns,
            "Missing Values": data.isnull().sum(),
            "Percentage (%)":
            (data.isnull().sum()/len(data)*100).round(2)
        }
    )


    st.dataframe(
        missing_values,
        use_container_width=True
    )



    # Statistical Summary

    st.subheader("📈 Statistical Summary")


    st.dataframe(
        data.describe(),
        use_container_width=True
    )



    st.write("---")


    st.success(
        "🚀 Dataset is ready for Data Cleaning, Dashboard and Machine Learning Modules"
    )



else:

    st.info(
        "📌 Please upload a CSV or Excel dataset to continue."
    )



