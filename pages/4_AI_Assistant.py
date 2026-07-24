import streamlit as st
import pandas as pd
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(
    page_title="MediVision AI Pro",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 MediVision AI Assistant")
st.caption(
    "🤖 Your intelligent healthcare data analysis assistant"
)
uploaded_file = st.file_uploader(
    "📂 Upload Hospital Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
        data["Gender"] = data["Gender"].astype(str).str.strip().str.title()
    else:
        data = pd.read_excel(uploaded_file)

    st.success("Dataset Loaded Successfully ✅")

st.write(
    "Welcome to MediVision AI Pro. Ask any question related to the hospital dataset."
)

st.write("---")

user_question = st.text_input(
    "💬 Ask MediVision AI about healthcare data"
)

ask_button = st.button("🚀 Ask AI")

st.write("---")

st.subheader("🤖 AI Response")


if ask_button:

    if uploaded_file is None:
        st.warning("⚠ Please upload the dataset first.")

    elif user_question.strip() == "":
        st.warning("⚠ Please enter a question.")

    else:

        question = user_question.lower()

        answer = ""

        if "total patients" in question:

            answer = f"👥 Total Patients : {len(data)}"

        elif "female patients" in question:

            female = (data["Gender"].str.lower() == "female").sum()

            answer = f"👩 Female Patients : {female}"

        elif "male patients" in question:

            male = (data["Gender"].str.lower() == "male").sum()

            answer = f"👨 Male Patients : {male}"

        elif "average age" in question:

            avg_age = round(data["Age"].mean(),2)

            answer = f"🎂 Average Age : {avg_age}"

        elif "total hospitals" in question:

            hospitals = data["Hospital"].nunique()

            answer = f"🏥 Total Hospitals : {hospitals}"

        elif "blood type" in question:

            blood = data["Blood Type"].value_counts().idxmax()

            answer = f"🩸 Most Common Blood Type : {blood}"

        elif "patient insights" in question:

            total = len(data)

            male = (data["Gender"].str.lower() == "male").sum()

            female = (data["Gender"].str.lower() == "female").sum()

            avg_age = round(data["Age"].mean(), 2)

            hospitals = data["Hospital"].nunique()

            blood = data["Blood Type"].value_counts().idxmax()


            answer = f"""
            📊 Patient Insights Summary

            👥 Total Patients : {total}

            👨 Male Patients : {male}

            👩 Female Patients : {female}

            🎂 Average Age : {avg_age}

            🏥 Total Hospitals : {hospitals}

            🩸 Common Blood Type : {blood}
            """
        
        else:

            answer = """❌ Sorry! I couldn't understand your question.

            You can ask me:
            👥 Total Patients
            👨 Male Patients
            👩 Female Patients
            🎂 Average Age
            🏥 Total Hospitals
            🩸 Blood Type
            """


        # Display AI Response
        if answer.startswith("❌"):
            st.error(answer)
        else:
            st.success(answer)


        # Save Chat History
        st.session_state.chat_history.append(
            {
                "question": user_question,
                "answer": answer
            }
        )

        if st.button("🗑️ Clear Chat"):

            st.session_state.chat_history = []

            st.success("Chat cleared successfully!")

            st.subheader("💬 Chat History")


            st.subheader("💬 Conversation History")

st.subheader("💬 MediVision AI Chat")

for chat in st.session_state.chat_history:

    st.markdown(
        f"""
        **👤 You:**  
        {chat['question']}
        """
    )

    st.markdown(
        f"""
        **🤖 MediVision AI:**  
        {chat['answer']}
        """
    )

    st.divider()
