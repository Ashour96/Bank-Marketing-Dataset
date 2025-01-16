import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
uploaded_file = r'F:\Amit Machine Learning\Projects\Bank Marketing Dataset\Final Data.csv'  # Replace with your uploaded file path
data = pd.read_csv(uploaded_file)

st.title("Bank Marketing Dataset")

st.header("Data Overview")
st.write("First rows in dataset:")
st.dataframe(data.head())


st.header("Summary Statistics")
st.dataframe(data.describe())



#spliting the data frame to categorycal and numerical
cat_col = ['job', 'marital', 'education', 'housing', 'loan', 'contact', 'day', 'month', 'deposit']
num_col = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous']
monthes = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

cat_data = data[cat_col]
num_data = data[num_col]

st.header("Custimize Data Show")
if st.checkbox('Show Numerical Data'):
    st.dataframe(num_data.head())

if st.checkbox('Show Categorical Data'):
    st.dataframe(cat_data.head())

if st.checkbox('Show Data acording to the date'):
    x = st.slider('month', min_value =0, max_value=11)
    st.write('returned month is : ', monthes[x])
    d = st.slider('day', min_value =1, max_value=31)
    month_df = data[(data['month'] == monthes[x]) & (data['day'] == d)]
    st.dataframe(month_df)
        


# Select Columns for Visualization
st.header("Data Visualization")
st.write("Select columns to visualize:")
plot_type = st.radio("Select Plot Type:", ["Scatter Plot", "Line Plot", "Histogram", "Count plot"])

# Plotting
if plot_type == "Scatter Plot":
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("X-axis", num_data.columns)
    y_axis = st.selectbox("Y-axis", num_data.columns)
    fig = plt.figure()
    sns.scatterplot(data=data, x=x_axis, y=y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type == "Line Plot":
    st.subheader("Line Plot")
    x_axis = st.selectbox("X-axis", num_data.columns)
    y_axis = st.selectbox("Y-axis", num_data.columns)
    fig = plt.figure()
    sns.lineplot(x=x_axis,y=y_axis,data=data)
    st.pyplot(fig)
elif plot_type == "Histogram":
    st.subheader("Histogram")
    x_axis = st.selectbox("X-axis", cat_data.columns)
    # y_axis = st.selectbox("Y-axis", data.columns)
    fig = plt.figure()
    sns.histplot(x=x_axis,data=data)
    plt.xlabel(x_axis)
    plt.ylabel("Frequency")
    st.pyplot(fig)
elif plot_type == "Count plot":
    st.subheader("Histogram")
    x_axis = st.selectbox("X-axis", cat_data.columns)
    y_axis = st.selectbox("hue", cat_data.columns)
    fig = plt.figure()
    # sns.histplot(x=x_axis,data=data)
    sns.countplot(x=x_axis,hue = y_axis,data=data, palette='tab10')
    plt.xlabel(x_axis)
    plt.ylabel("Frequency")
    st.pyplot(fig)

# Correlation Heatmap
st.header("Correlation Heatmap")
if st.button("Generate Heatmap"):
    numeric_data = data.select_dtypes(include=['number'])  # Select only numeric columns
    if numeric_data.empty:
        st.warning("No numeric columns found for correlation heatmap.")
    else:
        fig = plt.figure()
        sns.heatmap(numeric_data.corr(), annot=True, cmap="Reds")
        st.pyplot(fig)