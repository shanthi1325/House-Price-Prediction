# 🏠 House Price Prediction

## 📘 Overview
This project predicts house prices based on various features such as area, number of rooms, location, bathrooms, and balconies using Machine Learning. It also includes a 
**Streamlit web app** for interactive predictions.
## ⚙️ Technologies Used
- Python  
- Pandas & NumPy  
- Scikit-learn  
- Pickle (for saving/loading models)  
- Streamlit (for web app)  
- Jupyter Notebook / Google Colab  

## 🧹 Data Cleaning Process
Before training the model, the dataset (`Cleaned_data.csv`) was cleaned and preprocessed:  
1. **Missing Values:** Removed or imputed missing entries.  
2. **Outlier Removal:** Eliminated unrealistic values for `total_sqft`, `Bedroom`, `bath`, and `balcony`.  
3. **Standardization:** Converted area to consistent units (e.g., square feet).  
4. **Categorical Encoding:** Processed `location` for model input.  
5. **Saved Cleaned Data:** The cleaned dataset is saved as `Cleaned_data.csv` for model training.

## 🧠 Model Description
The project uses regression models to predict house prices.  
- The trained model is saved as `House_prediction_model.pkl`.  
- Performance metrics such as **R² Score**, **MAE**, and **RMSE** are used to evaluate the model.

## 📊 Dataset
The dataset (`Cleaned_data.csv`) contains information about house features and prices.  

Columns include:  
- `location`  
- `total_sqft`  
- `Bedroom`  
- `bath`  
- `balcony`  

## 🚀 How to Run the Streamlit App
1. Make sure you have Streamlit installed and run:
   ```bash
   pip install streamlit
   streamlit run app.py  
**Power BI dashboard** for visual analysis of house prices.  
## 📊 Power BI Dashboard
A **House Price Dashboard** is created using Power BI.
**Features include:**
- Distribution of house prices by location.
- Price trends based on area, bedrooms, bathrooms, and balconies.
- Interactive visualizations and slicers for filtering.
The dashboard helps in analyzing patterns and insights before making predictions.
<img width="1920" height="1080" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/a25e9c0c-ba86-4fe4-a19d-49dd466d89ae" />

