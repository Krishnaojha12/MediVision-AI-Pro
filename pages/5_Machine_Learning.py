import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



st.set_page_config(
    page_title="Machine Learning",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Machine Learning Module")

uploaded_file = st.file_uploader(
    "📂 Upload Hospital Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.success("Dataset Loaded Successfully ✅")

    st.write("---")

    st.subheader("Dataset Preview")

    st.dataframe(data.head())

    st.write("---")

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", data.shape[0])

    with col2:
        st.metric("Columns", data.shape[1])

    st.write("---")

    st.subheader("Selected Features")

    features = [
        "Age",
        "Gender",
        "Blood Type",
        "Medical Condition",
        "Admission Type",
        "Insurance Provider",
        "Medication"
    ]

    st.write(features)

    st.write("---")

    st.subheader("Target Variable")

    target = "Billing Amount"

    st.success(target)

    st.write("---")

    st.subheader("Label Encoding")

    encode_data = data.copy()

    label_encoder = LabelEncoder()

    categorical_columns = [
        "Gender",
        "Blood Type",
        "Medical Condition",
        "Admission Type",
        "Insurance Provider",
        "Medication"
]

    for column in categorical_columns:

        encode_data[column] = label_encoder.fit_transform(encode_data[column])
    

    st.success("Label Encoding Completed Successfully ✅")

    st.subheader("Encoded Dataset Preview")

    st.dataframe(encode_data.head())

    st.write("---")

    st.subheader("Train Test Split")

    X = encode_data[features]

    y = encode_data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    st.success("Train Test Split Completed Successfully ✅")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Training Rows", X_train.shape[0])

    with col2:
        st.metric("Testing Rows", X_test.shape[0])

    st.write("---")

    st.subheader("Linear Regression Model")

    model = LinearRegression()

    model.fit(X_train, y_train)

    st.success("Linear Regression Model Trained Successfully ✅")

    st.write("Model is now ready for prediction.")


    st.write("---")

    st.subheader("Billing Amount Prediction")

    age = st.number_input("Age", min_value=1, max_value=100, value=30)

    gender = st.selectbox("Gender", ["Male", "Female"])

    blood = st.selectbox(
        "Blood Type",
        sorted(data["Blood Type"].unique())
    )

    condition = st.selectbox(
        "Medical Condition",
        sorted(data["Medical Condition"].unique())
    )

    admission = st.selectbox(
        "Admission Type",
        sorted(data["Admission Type"].unique())
    )

    insurance = st.selectbox(
        "Insurance Provider",
        sorted(data["Insurance Provider"].unique())
    )

    medication = st.selectbox(
        "Medication",
        sorted(data["Medication"].unique())
    )

    if st.button("Predict Billing Amount"):

        input_data = pd.DataFrame({
            "Age": [age],
            "Gender": [gender],
            "Blood Type": [blood],
            "Medical Condition": [condition],
            "Admission Type": [admission],
            "Insurance Provider": [insurance],
            "Medication": [medication]
        })

        for column in categorical_columns:
            input_data[column] = label_encoder.fit_transform(
                pd.concat([data[column], input_data[column]])
            )[-1:]

        prediction = model.predict(input_data)

        st.success(f"💰 Predicted Billing Amount : {prediction[0]:.2f}")



    st.write("---")

    st.subheader("Model Accuracy")

    y_pred = model.predict(X_test)

    accuracy = r2_score(y_test, y_pred)

    st.success(f"R² Score : {accuracy:.4f}")

    # if accuracy >= 0.90:
    #     st.success("Excellent Model Performance ✅")
    # elif accuracy >= 0.70:
    #     st.warning("Good Model Performance 👍")
    # else:
    #     st.error("Model Needs Improvement ❌")

    st.write("---")

    st.subheader("💾 Save Machine Learning Model")

    if st.button("Save Model"):

        joblib.dump(model, "models/billing_model.pkl")

        st.success("Model Saved Successfully ✅")

    st.write("---")

    st.subheader("📂 Load Saved Model")

    if st.button("Load Saved Model"):

        loaded_model = joblib.load("models/billing_model.pkl")

        st.success("Model Loaded Successfully ✅")
