import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open(r'C:\Users\shant\OneDrive\Desktop\house_price_prediction\House_prediction_model.pkl', 'rb'))

st.header("House Price Prediction")
data = pd.read_csv(r'Cleaned_data.csv')

loc= st.selectbox("Choose a city", data['location'].unique())
sqft = st.number_input("Enter the area in square feet")
beds = st.number_input("Enter the number of BHK")
bath = st.number_input("Enter the number of bathrooms")
balc = st.number_input("Enter the number of balconies")

input = pd.DataFrame([[loc, sqft, beds, bath, balc]], columns=['location', 'total_sqft', 'Bedroom', 'bath', 'balcony'])

if st.button("Predict"):
	prediction = model.predict(input)
	out_str = 'Price of the house is: '+ str(prediction[0]*100000) + ' lakhs'
	st.success(out_str)