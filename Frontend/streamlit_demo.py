# streamlit_demo.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import numpy as np
import pandas as pd
import streamlit_authenticator as stauth
from PIL import Image
import requests

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)
table_id = 'recipe-recommendation-348000.get_cooking.users'

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.experimental_memo to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

fullnames = run_query("SELECT fullname FROM " + table_id +  " LIMIT 10")
password_rows = run_query("SELECT password FROM " + table_id + " LIMIT 10")
password = []
names = []
unames = []
uname = run_query("SELECT username FROM " + table_id + " LIMIT 10")

# Print results.
st.write("Some wise words from Shakespeare:")
for row in password_rows:
    password.append(row['password'])
    st.write("✍️ " + row['password'])

for row in fullnames:
    names.append(row['fullname'])

for row in uname:
    unames.append(row['username'])

# with st.container():
#     st.write("This is inside the container")

#     # You can call any Streamlit command, including custom components:
#     st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")

# names = ['Niramay Kelkar','Jurgen Klopp']
# usernames = ['nkelkar','jklopp']
# passwords = ['111','222']

hashed_passwords = stauth.Hasher(password).generate()

authenticator = stauth.Authenticate(names,unames,hashed_passwords,
    'stauth','mysecretkey',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')

if authentication_status:
    st.write("Success")
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    image = 'https://storage.cloud.google.com/get-cooking/image.jpeg'
    st.image(image, caption='', width=700)
    st.title('Get Cooking')
    st.write('An ML powered app!')

    title = st.text_input('Recipe Name', '', placeholder='Enter the keyword')
    st.write('The current recommendations is for ', title)
   
    if st.button('Submit'):
        res = requests.get(f"http://127.0.0.1:8000/{title}")
        output = pd.read_csv(res)
        print(output)
        out = output.get("message")
        # df = pd.read_csv('https://storage.googleapis.com/get-cooking/dataset/RAW_recipes.csv')
        
        st.write("Success")
        # sample_data = df.head()
        # st.dataframe(sample_data)
        #     st.write("Success")
        st.write('The current recommendations is for ', out)

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
    