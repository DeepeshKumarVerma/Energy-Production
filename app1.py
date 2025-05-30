import streamlit as st
import pickle
import numpy as np

# Load the pickled model
with open(r'C:\Users\DELL\Desktop\P_324_Regression_Energy_Production\deployment\random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Custom CSS for dark theme
custom_css = """
    body {
        background-color: #1E1E1E;
        color: white;
    }
    .st-bw {
        background-color: #272727 !important;
        color: white !important;
    }
"""

# Apply the custom CSS
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

st.title('🌲 Combine Cycle Power Plant Energy Prediction 🌳')

# Input box for user input
st.header('🚀 Enter Test Values 🚀')

# Assuming you have the same features as in your training data
tempreture = st.text_input('🌡️ Temperature', '5.0')
exhaust_vac = st.text_input('💨 Exhaust Vacuum', '5.0')
amb_pre = st.text_input('🌍 Ambient Pressure', '5.0')
r_humidity = st.text_input('💧 Relative Humidity', '5.0')

# Convert user input to float
tempreture = float(tempreture)
exhaust_vac = float(exhaust_vac)
amb_pre = float(amb_pre)
r_humidity = float(r_humidity)

# Predict button with animation
if st.button('🔮 Predict Energy Production'):
    # Create a numpy array from the user input
    input_data = np.array([[tempreture, exhaust_vac, amb_pre, r_humidity]])

    # Make predictions
    prediction = model.predict(input_data)

    # Display the input values
    st.subheader('📊 Input Values:')
    st.write(f'🌡️ Temperature: {tempreture}')
    st.write(f'💨 Exhaust Vacuum: {exhaust_vac}')
    st.write(f'🌍 Ambient Pressure: {amb_pre}')
    st.write(f'💧 Relative Humidity: {r_humidity}')

    # Display the prediction with an animation
    st.subheader('🎯 Energy Prediction:')
    st.write(f'🔮 The predicted output is: {prediction[0]}')

    # Add cool animations
    st.balloons()
