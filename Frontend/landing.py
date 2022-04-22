from logging import PlaceHolder
import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
image = 'https://storage.cloud.google.com/get-cooking/image.jpeg'
st.image(image, caption='', width=700)

st.title('Get Cooking')
st.write('An ML powered app!')

title = st.text_input('Recipe Name', '', placeholder='Enter the keyword')
st.write('The current recommendations is for ', title)