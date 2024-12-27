import streamlit as st
import pandas as pd
import joblib
pipeline = joblib.load('movie_rating_pipeline.pkl')
st.title("Movie Rating Classifier")
st.write("Classify movies into High or Medium ratings based on Ranking and Genre.")
ranking = st.number_input("Enter the Ranking (e.g., 50):", min_value=1, step=1)
genre = st.selectbox("Select the Genre:", ["Action", "Drama", "Comedy", "Thriller", "Horror"])
if st.button("Predict"):
     new_data = pd.DataFrame({'Ranking': [ranking], 'Genre': [genre]})
     prediction = pipeline.predict(new_data)
     st.success(f"The predicted rating category is: {prediction[0]}")
     
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)