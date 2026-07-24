import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Cleaning",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Data Cleaning Module")

uploaded_file = st.file_uploader(
    "📂 Upload Hospital Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    clean_data = data.copy()

    st.success("✅ Hospital Dataset Uploaded Successfully")
    st.info("📊 Dataset is ready for Analysis")

    st.write("---")

    st.subheader("📄 Dataset Preview")

    st.dataframe(clean_data.head())

    st.write("---")

    st.subheader("📊 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Rows", clean_data.shape[0])

    with col2:
        st.metric("Total Columns", clean_data.shape[1])

    st.write("---")

    st.subheader("📋 Column Names")

    st.write(list(clean_data.columns))

    st.write("---")

    st.subheader("📝 Data Types")

    st.dataframe(clean_data.dtypes)

    st.write("---")

    st.subheader("❌ Missing Values")

    st.dataframe(clean_data.isnull().sum())

    st.write("---")

    st.subheader("♻ Duplicate Records")

    duplicate = clean_data.duplicated().sum()

    st.metric("Duplicate Rows", duplicate)

    st.write("---")

    st.subheader("📈 Dataset Statistics")

    st.dataframe(clean_data.describe())


    st.write("---")

    st.subheader("🧹 Data Cleaning")

if st.button("Remove Missing Values"):
    clean_data = clean_data.dropna()
    st.success("🧹 Missing Values Removed Successfully")
    st.info("Clean Dataset is Ready")

if st.button("Remove Duplicate Rows"):
    clean_data = clean_data.drop_duplicates()
    st.success("Duplicate Rows Removed Successfully ✅")

    st.write("---")

    st.subheader("📊 Cleaned Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", clean_data.shape[0])

    with col2:
        st.metric("Columns", clean_data.shape[1])

    st.write("---")

    st.subheader("📄 Cleaned Dataset Preview")

    st.dataframe(clean_data.head())

    st.write("---")

    csv = clean_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
)

    st.write("----")

    st.subheader("📋 Cleaned Dataset Summary")

    st.write(f"📄 Total Rows : {len(clean_data)}")
    st.write(f"📋 Total Columns : {len(clean_data.columns)}")

    st.write("Column Names")
    st.write(list(clean_data.columns))

    st.subheader("First 10 Records")

    st.dataframe(clean_data.head(10))