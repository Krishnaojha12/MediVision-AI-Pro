import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Upload",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Hospital Dataset Upload")

st.write("Upload your Hospital CSV or Excel Dataset")

st.write("---")

uploaded_file = st.file_uploader(
    "Choose CSV or Excel File",
    type=["csv", "xlsx"]

)

if uploaded_file is not None:

    try:

        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)

        else:
            data = pd.read_excel(uploaded_file)

            if data.empty:
                

                st.error("❌ Uploaded Dataset is Empty")

                st.stop()


    except Exception:

        st.error("❌ Invalid Dataset or File Format")
        st.stop()

    st.subheader("📋 Dataset Preview")

    st.dataframe(data)

    rows, cols = data.shape

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Rows", rows)

    with col2:
        st.metric("Total Columns", cols)

    st.subheader("📝 Column Names")

    st.write(list(data.columns))

    st.subheader("🔝 First 5 Rows")

    st.dataframe(data.head())

    st.subheader("🔚 Last 5 Rows")

    st.dataframe(data.tail())

    st.subheader("📊 Dataset Shape")

    st.write(f"Rows : {data.shape[0]}")

    st.write(f"Columns : {data.shape[1]}")

    st.subheader("📑 Data Types")

    st.dataframe(data.dtypes.astype(str))

    st.subheader("❓ Missing Values")

    missing_values = data.isnull().sum().reset_index()

    missing_values.columns = ["Column Name", "Missing Values"]

    st.dataframe(missing_values)

    st.subheader("📈 Statistical Summary")

    st.dataframe(data.describe())