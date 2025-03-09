"""
# My first app
Here's our first attempt at using data to create a table:

"""

import streamlit as st
import pandas as pd
import numpy as np

#df = pd.DataFrame({
#    'First column': [1,2,3,4,5,6],
#    'Second column': [10,20,30,40,50,60]
#})

#df

#st.write("Here is our first attempt at using data to create a table")
#st.write(pd.DataFrame({
#    'First column': [1,2,3,4,5,6],
#    'Second column': [10,20,30,40,50,60]
#}))

dataframe = pd.DataFrame(np.random.randn(10,20),
columns=('col %d' % i for i in range (20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Line chart")
chartdata = pd.DataFrame(np.random.randn(20,3),
columns = ['a', 'c', 'd'])

st.line_chart(chartdata)

st.write("Plot map")

mapdata = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(mapdata)

x = st.slider('x')
st.write(x, 'square is ', x * x)

st.text_input("Your name", key='name')
st.session_state.name