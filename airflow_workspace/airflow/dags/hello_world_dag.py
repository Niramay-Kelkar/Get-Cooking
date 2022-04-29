from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print("Hello World")

with DAG(dag_id="hello_world_dag",
         start_date=datetime(2021,4,27),
         schedule_interval='*/2 * * * *',
         catchup=False) as dag:

        task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld)

task1
# #import config, rec_sys
# #from rec.ingredient_parser import ingredient_parser
# import pandas as pd
# #from sklearn.feature_extraction.text import TfidfVectorizer
# #from sklearn.metrics.pairwise import cosine_similarity  
# #from ingredient_parser import ingredient_parser
# import pickle
# #import config 
# #import unidecode, ast
# import random

# def helloWorld():
#     #ingredients = ['chicken','tofu','pineapple']
#     print("Hello World")
#     #i= random.choice(ingredients)
#     #recipe = rec_sys.RecSys(i)
#     #recipe.to_csv (r'export_dataframe.csv', index = False, header=True)




# with DAG(dag_id="food_rec_dag",
#          start_date=datetime(2022,4,26),
#          schedule_interval='*/5 * * * *',
#          catchup=False) as dag:

#         task1 = PythonOperator(
#         task_id="food_rec",
#         python_callable=helloWorld)


# task1
