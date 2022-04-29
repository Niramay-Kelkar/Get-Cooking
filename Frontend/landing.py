from logging import PlaceHolder
import streamlit as st
import pandas as pd
import numpy as np
import requests
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image


#Authentication using JWT tokens in Streamlit
#Reference link: https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031

names = ['Niramay Kelkar','Jurgen Klopp']
usernames = ['nkelkar','jklopp']
passwords = ['123','456']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'stauth','mysecretkey',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')


if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    image = 'https://storage.cloud.google.com/get-cooking/image.jpeg'
    st.image(image, caption='', width=700)
    st.title('Get Cooking')
    st.write('An ML powered app!')

    title = st.text_input('Recipe Name', '', placeholder='Enter the keyword')
    st.write('The current recommendations is for ', title)
   
    if st.button('Submit'):
        # res = requests.get(f"http://127.0.0.1:8000/{title}")
        # output = pd.read_csv(res)
        # print(output)
        # out = output.get("message")
        df = pd.read_csv('https://storage.googleapis.com/get-cooking/dataset/RAW_recipes.csv')
        
        st.write("Success")
        sample_data = df.head()
        st.dataframe(sample_data)
        #     st.write("Success")
        #st.write('The current recommendations is for ', out)

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

