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
        n_rec = st.text_input("Enter number of recipes you want")
        execute_recsys = st.button("Give me recommendations!")

        if execute_recsys:
            
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


       
        









   





if __name__ == "__main__":
    main()
