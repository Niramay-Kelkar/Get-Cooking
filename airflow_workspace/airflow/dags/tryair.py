import config, rec_sys
from ingredient_parser import ingredient_parser
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from ingredient_parser import ingredient_parser
import pickle
import config 
import unidecode, ast
import random
def helloWorld():
    ingredients = ['chicken','tofu','pineapple']
    #print(‘Hello World’)
    i= random.choice(ingredients)
    recipe = rec_sys.RecSys(i)
    recipe.to_csv (r'export_dataframe.csv', index = False, header=True)



helloWorld()