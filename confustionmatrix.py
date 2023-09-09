import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
def test5():

    data = pd.read_csv('diabetes.csv')

    corr_mat = data.corr()
    plt.figure(figsize=(10,10))
    sns.heatmap(corr_mat,annot=True,cmap='RdYlGn')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
