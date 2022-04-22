from logging import PlaceHolder
import streamlit as st
import pandas as pd
import numpy as np

st.title('Get Cooking')
st.write('An ML powered app!')

title = st.text_input('Recipe Name', '', placeholder='Enter the keyword')
st.write('The current recommendations is for ', title)