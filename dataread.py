# from google.cloud import bigquery



# def query_stackoverflow():
#     client = bigquery.Client()
#     query_job = client.query(
#         """
#         SELECT
#           CONCAT(
#             'https://stackoverflow.com/questions/',
#             CAST(id as STRING)) as url,
#           view_count
#         FROM `bigquery-public-data.stackoverflow.posts_questions`
#         WHERE tags like '%google-bigquery%'
#         ORDER BY view_count DESC
#         LIMIT 10"""
#     )

#     results = query_job.result()  # Waits for job to complete.

#     for row in results:
#         print("{} : {} views".format(row.url, row.view_count))


# if __name__ == "__main__":
#     query_stackoverflow()

from google.cloud import bigquery
import os

credentials_path = "/Users/niramaykelkar/Desktop/DAMG7245/Get-Cooking/recipe-recommendation-348000-4111a3a0d8a1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'recipe-recommendation-348000.get_cooking.users'

rows_to_insert = [
    {'username': 'jdoe', 'email': 'jdoe@example.com', 'fullname': 'John Doe', 'password': 'abcd', 'disabled': False, 'apihits': 1},
    {'username': 'dcosta', 'email': 'dcosta@example.com', 'fullname': 'Douglas Costa', 'password': 'dcos', 'disabled': True, 'apihits': 2},
]

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors==[]:
    print('New rows added')
else:
    print('Error')
