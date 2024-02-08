import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('IRIS FLOWER DASHBOARD')
st.divider()
df=pd.read_csv("C:/Users/User20/Downloads/Iris (1).csv")
st.sidebar.header('Description :::')
st.sidebar.markdown('The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems. It is sometimes called Anderson Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. The data set consists of 50 samples from each of three species of Iris (Iris Setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.')
col1,col2=st.columns(2)
with col1:
    st.subheader('Pie Chart of species')
    
with col2:
    st.subheader('Bar Chart of Species')