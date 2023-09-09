import pandas as pd
import streamlit as st
import pyperpclip
from streamlit_option_menu import option_menu
from test import test1
from home import test2
from flow import test3
from visualize import test4
st.set_page_config(page_title='Diabetes Prediction App', page_icon=':bar_chart:', layout='wide')
st.title('Diabetes prediction using data mining')

choice = option_menu(
        menu_title='Main Menu',
        options=['Home','Predict','Work flow','Visualize','Dataset'],
        menu_icon='cursor-fill',
        icons=['house','check2-square','diagram-2-fill','eye','file-earmark'],
        default_index=0,
        orientation = 'horizontal',
)

if choice == 'Home':
    test2()
if choice == 'Predict':
    test1()
if choice == 'Work flow':
    test3()
if choice == 'Visualize':
    test4()
if choice == 'Dataset':
    st.header('Dataset')
    data = pd.read_csv('diabetes.csv')
    st.subheader('Features:')
    for i in data.columns:
        st.write("   -->",i)
    st.subheader('Description:')
    st.table(data.describe().T)
    st.subheader('Dataset:')
    st.dataframe(data)





