import streamlit as st
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Breast Cancer Prediction System")

st.info("Upload Breast Cancer Wisconsin Dataset (.csv)")

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully ✅")

    st.write("---")


    # DATASET PREVIEW

    st.subheader("📋 Dataset Preview")

    st.dataframe(data.head())

    st.write("---")


    # DATASET SHAPE
    st.subheader("📏 Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", data.shape[0])

    with col2:
        st.metric("Columns", data.shape[1])

    st.write("---")

    # DATA CLEANING
    st.subheader("🧹 Data Cleaning")

    # Remove unnecessary columns
    if "id" in data.columns:
        data.drop(columns=["id"], inplace=True)

    if "Unnamed: 32" in data.columns:
        data.drop(columns=["Unnamed: 32"], inplace=True)

    st.success("Unused Columns Removed Successfully ✅")

    st.write("---")


    # LABEL ENCODING
    st.subheader("🔤 Label Encoding")

    encoder = LabelEncoder()

    data["diagnosis"] = encoder.fit_transform(
        data["diagnosis"]
    )

    st.success("Diagnosis Encoded Successfully ✅")

    st.write("---")


    # FEATURES & TARGET
    st.subheader("🎯 Features & Target")

    X = data.drop(columns=["diagnosis"])

    y = data["diagnosis"]

    st.write(f"Total Features : {X.shape[1]}")
    st.write(f"Target Variable : diagnosis")

    st.write("---")


    # TRAIN TEST SPLIT
    st.subheader("✂ Train Test Split")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    st.success("Train Test Split Completed Successfully ✅")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Training Rows", X_train.shape[0])

    with col2:
        st.metric("Testing Rows", X_test.shape[0])

    st.write("---")


    model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    max_depth=10
)

    model.fit(X_train, y_train)

    st.success("Model Trained Successfully ✅")
    st.write("---")

    st.subheader("🩺 Cancer Prediction")

    radius_mean = st.number_input(
        "Radius Mean",
        value=float(data["radius_mean"].mean())
    )

    texture_mean = st.number_input(
        "Texture Mean",
        value=float(data["texture_mean"].mean())
    )

    perimeter_mean = st.number_input(
        "Perimeter Mean",
        value=float(data["perimeter_mean"].mean())
    )

    area_mean = st.number_input(
        "Area Mean",
        value=float(data["area_mean"].mean())
    )

    smoothness_mean = st.number_input(
        "Smoothness Mean",
        value=float(data["smoothness_mean"].mean())
    )

    compactness_mean = st.number_input(
        "Compactness Mean",
        value=float(data["compactness_mean"].mean())
    )

    if st.button("Predict Cancer"):

        input_data = pd.DataFrame([X.mean()])

        input_data["radius_mean"] = radius_mean
        input_data["texture_mean"] = texture_mean
        input_data["perimeter_mean"] = perimeter_mean
        input_data["area_mean"] = area_mean
        input_data["smoothness_mean"] = smoothness_mean
        input_data["compactness_mean"] = compactness_mean

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("🔴 Malignant Cancer Detected")
        else:
            st.success("🟢 Benign (No Cancer Detected)")


    y_pred = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    st.write("---")

    st.subheader("📊 Model Accuracy")

    st.success(
        f"Accuracy : {accuracy*100:.2f}%"
    )

    st.write("---")

    st.subheader("📊 Confusion Matrix")

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    cm_df = pd.DataFrame(
        cm,
        index=[
            "Actual Benign",
            "Actual Malignant"
        ],
        columns=[
            "Predicted Benign",
            "Predicted Malignant"
        ]
    )

    st.dataframe(cm_df)

    st.write("---")

    st.subheader("📄 Classification Report")

    report = classification_report(
        y_test,
        y_pred,
        output_dict=True
    )

    report_df = pd.DataFrame(report).transpose()

    st.dataframe(report_df)

    st.write("---")

    st.subheader("⭐ Feature Importance")

    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    st.dataframe(importance)

    st.write("---")

    if st.button(
        "Save Model",
        key="save_model"
    ):

        os.makedirs(
            "models",
            exist_ok=True
        )

        joblib.dump(
            model,
            "models/breast_cancer_model.pkl"
        )

        st.success(
            "Model Saved Successfully ✅"
        )

    if st.button(
        "Load Model",
        key="load_model"
    ):

        loaded_model = joblib.load(
            "models/breast_cancer_model.pkl"
        )

        st.success(
            "Model Loaded Successfully ✅"
        )
        