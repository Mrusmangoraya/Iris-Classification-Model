import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
st.title("Iris Flower Classification")
st.write("This app classifies iris flowers based on their features.")

# Sidebar for user input
st.sidebar.header("User Input Features")
def user_input_features():
    sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
    sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 5.0, 3.0)
    petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.5)
    petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)
    
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    features=pd.DataFrame(data, index=[0])
    return features

df=user_input_features()

st.subheader("User Input Features")
st.write(df)

iris = sns.load_dataset("iris")
st.subheader("Iris Dataset")
st.write(iris.head())

st.subheader("Iris Dataset Visualization")

fig=px.bar(iris, x="species", y="sepal_width", color="species")
st.plotly_chart(fig)


st.subheader("seaborn plot")
sns.barplot(x="species", y="sepal_length", data=iris)
plt.title("Sepal Length by Species")
st.pyplot(plt)

x=iris[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y=iris["species"]


# Train the model
model = RandomForestClassifier()
model.fit(x, y)

prediction = model.predict(df)
pricdition_proba = model.predict_proba(df)
st.subheader("Class labels and their corresponding index number")
st.write(iris['species'].unique())

st.subheader("Prediction")

p=st.write(prediction[0])
st.write(p)

st.subheader("Prediction Probability")
st.write(pricdition_proba)


