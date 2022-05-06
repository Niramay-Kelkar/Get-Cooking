import streamlit as st
import pandas as pd
import numpy as np

import os
from PIL import Image


from ingredient_parser import ingredient_parser

from Food_Search import *

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('/')[5]
    return f'<a target="_blank" href="{link}">{text}</a>'

def validate_phone(phone_number):
    if len(phone_number)<10:
        raise ValueError("Phone number cannot be less than 10")



def main():
    image = Image.open("input/wordcloud.png").resize((680, 350))
    st.image(image)
    st.markdown("# *Get Cooking! :cooking:*")

    
    st.markdown(
        "## You have the ingredients, we have the recipes for you! :genie: "
    )
    st.markdown(
        "### Given a list of ingredients, what different recipes can you make? :stew: "
    )
    
    st.markdown(
        "For example, what recipes can you make with the food in your kitchen? :bento: Our app will look through over thousands of recipes to find top matches for you! :mag: Try it out for yourself below! :arrow_down:"
    )

    st.text("")



    #listindex=[]

    selection = st.selectbox(
     'Do you have any ingredients? Worry not if you do no have them; we will suggest you some easy recipes!',
     ('Yes', 'No'))

    if selection == 'Yes':
        ingredients = st.text_input("Enter ingredients you would like to cook with")
        if str(ingredients).isnumeric():
            st.write("Enter valid ingredient!")
        n_rec = st.text_input("Enter number of recipes you want")
        execute_recsys = st.button("Give me recommendations!")

        if execute_recsys :
            if int(n_rec)>0:

            
                ingred = ingredients.split(", ")
                n_rec = int(n_rec)
                col1, col2, col3 = st.columns([1, 6, 1])
                with col2:
                    gif_runner = st.image("input/cooking_gif.gif")
                recipe = search_ingredients(ingred , n_rec)
                #recipe.set_index([pd.Index(listindex)])
                # link is the column with hyperlinks
                recipe['recipe_urls'] = recipe['recipe_urls'].apply(make_clickable)
                recipe = recipe.to_html(escape=False)
                st.write(recipe, unsafe_allow_html=True)


                gif_runner.empty()
            
            elif int(n_rec) ==0: 
                st.write("Please provide a value greater than zero. ")
            
            else:
                st.write("Please provide a valid input")
            
            #st.dataframe(recipe) 

    if selection == "No":

        from google.cloud import storage

        import os
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="bigdataproject-349122-0d6e9f2cf566.json"
        client = storage.Client()

        bucket = client.get_bucket('us-east1-airflowenv-ce25265b-bucket')

        blob = bucket.get_blob('dags/export_dataframe.csv')

        downloaded_blob = blob.download_as_string()
        print(downloaded_blob)
        print("-----------BLOB------------")
        print(type(downloaded_blob))
        from io import StringIO

        s=str(downloaded_blob,'utf-8')

        downloaded_blob = StringIO(s) 


        df_random=pd.read_csv(downloaded_blob)

        st.write(df_random)


    st.markdown("### Browse collections! :eyes: ")


    col11, col12, col13 = st.columns([1, 6, 1])
    with col12:
        gif_runner = st.image("input/collections.gif")


    option = st.selectbox(
     'Browse recipe collections!',
     ('Seafood', 'Soup', 'Curry', 'Pasta', 'Salad', 'Chinese'))

    
    st.write('You selected:', option)
    
    execute_browse = st.button("Browse!")


    if execute_browse:
        print(option)


        if option == "Seafood":
            
            collection = search_collections(option)
            collection['recipe_urls'] = collection['recipe_urls'].apply(make_clickable)
            collection = collection.to_html(escape=False)
            st.write(collection, unsafe_allow_html=True)
        
        if option == "Soup":
            
            collection = search_collections(option)
            collection['recipe_urls'] = collection['recipe_urls'].apply(make_clickable)
            collection = collection.to_html(escape=False)
            st.write(collection, unsafe_allow_html=True)


        if option == "Curry":
            
            collection = search_collections(option)
            collection['recipe_urls'] = collection['recipe_urls'].apply(make_clickable)
            collection = collection.to_html(escape=False)
            st.write(collection, unsafe_allow_html=True)


        if option == "Pasta":
            
            collection = search_collections(option)
            collection['recipe_urls'] = collection['recipe_urls'].apply(make_clickable)
            collection = collection.to_html(escape=False)
            st.write(collection, unsafe_allow_html=True)
        
        if option == "Salad":
            
            collection = search_collections(option)
            collection['recipe_urls'] = collection['recipe_urls'].apply(make_clickable)
            collection = collection.to_html(escape=False)
            st.write(collection, unsafe_allow_html=True)


        if option == "Chinese":
            
            collection = search_collections(option)
            collection['recipe_urls'] = collection['recipe_urls'].apply(make_clickable)
            collection = collection.to_html(escape=False)
            st.write(collection, unsafe_allow_html=True)

    with st.sidebar.expander("How it works?", expanded=True):
        st.markdown("## How it works? :thought_balloon:")
        st.write(
            "For an in depth overview of how we created this app, refer the link below."
        )
        blog1 = "https://codelabs-preview.appspot.com/?file_id=10H0eKtgY-nI27dKWndBheBJevna_0GfMpCd6DrCE-sg#1"
        
        st.markdown(
            f" [Building a Recipe Recommendation App]({blog1})"

        )

        st.write("### Register here for weekly recipe collections!")
        firstname = st.text_input("Enter First Name")
        lastname = st.text_input("Enter Last Name")
        email = st.text_input("Enter email")
        
        import re
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if (re.fullmatch(regex, email))== None:
            st.write("Enter a valid email address")

        phone_number = st.text_input("Enter phone number")

        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        if Pattern.match(phone_number) == None:
            st.write("Enter valid phone number")

        location = st.text_input("Enter location")

        satisfaction = st.selectbox(
        'Satisfied with the app?',
        ('Yes', 'No'))


        execute_register = st.button("Register!")

        if execute_register:
            user_register_entry = []
            user_register_entry.append(firstname)
            user_register_entry.append(lastname)
            user_register_entry.append(email)
            user_register_entry.append(phone_number)
            user_register_entry.append(location)
            user_register_entry.append(satisfaction)

            #Writing user register details into a text file
            # a for appending
            #w if no file exists
            with open("user_register.txt", "a") as output:      
                #output.write(user_register_entry)

                for item in user_register_entry:
                    output.write("%s," % item)
                output.write("\n")

            import pandas as pd
            df_user_registry = pd.read_csv(
                'user_register.txt', sep=",",header=None)
            
            df_user_registry.to_csv("df_user_register.csv", sep='\t')

            #Uploading into cloud
            import json
            from google.cloud import storage
            from google.oauth2 import service_account

            project_id = "BigDatatProject"
            path_to_token = './bigdataproject-349122-0d6e9f2cf566.json'

            storage_credentials= service_account.Credentials.from_service_account_file(path_to_token)
            storage_client = storage.Client(project=project_id, credentials = storage_credentials)

            #Destination

            destination_bucket_name = "results_food_rec"
            destination_bucket = storage_client.bucket(destination_bucket_name)


            destination_blob_name = 'df_user_register.csv'
            blob = destination_bucket.blob(destination_blob_name)


            source_file_name = "df_user_register.csv"
            blob.upload_from_filename('df_user_register.csv')

        




       
        









   





if __name__ == "__main__":
    main()
