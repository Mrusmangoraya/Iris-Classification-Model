# 🌸 Iris Flower Classification App

This Streamlit web application classifies iris flowers into three species — *setosa*, *versicolor*, and *virginica* — based on user-input flower measurements. It uses a Random Forest classifier and provides both prediction and probability estimates along with data visualizations.

##  Features

- **Interactive User Input**  
  Easily input flower measurements (sepal and petal dimensions) using sliders.

- **Live Prediction**  
  Get real-time classification results using a trained `RandomForestClassifier`.

- **Prediction Probability**  
  View the confidence scores for each predicted class.

- **Dataset Overview**  
  Displays the first few rows of the built-in Iris dataset from Seaborn.

- **Data Visualizations**  
  - Bar chart of average sepal width by species using Plotly  
  - Bar chart of average sepal length by species using Seaborn and Matplotlib

## 🧠 Model

- **Algorithm:** Random Forest Classifier  
- **Target Variable:** Species (`setosa`, `versicolor`, `virginica`)  
- **Input Features:**  
  - Sepal Length (cm)  
  - Sepal Width (cm)  
  - Petal Length (cm)  
  - Petal Width (cm)

## 🛠️ Requirments

Ensure you have the following Python libraries installed:

```bash
pip install streamlit scikit-learn pandas seaborn matplotlib plotly
