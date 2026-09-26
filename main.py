import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🎓 Student Placement Prediction App")

st.write("Enter student details below to predict placement outcome:")

# Input fields
cgpa = st.number_input("Enter CGPA:", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter IQ:", min_value=50.0, max_value=200.0, step=1.0)

# Predict button
if st.button("Predict Placement"):
    # Prepare input for model
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Student will be placed!")
    else:
        st.error("❌ Student will not be placed.")
