
'''
from gcloud import storage

client = storage.Client()

bucket = client.get_bucket('food_recommendation')

blob = bucket.blob('my-test-file.txt')

filename = "%s/%s" % (folder, filename)
blob = bucket.blob(filename)

# Uploading string of text
blob.upload_from_string('this is test content!')

# Uploading from a local file using open()
with open('export_dataframe.csv', 'rb') as f:
    blob.upload_from_file(f)

# Uploading from local file without open()
blob.upload_from_filename('export_dataframe.csv')

blob.make_public()
url = blob.public_url'''


import json
from google.cloud import storage
from google.oauth2 import service_account

project_id = "My First Project"
path_to_token = './bamboo-clone-340802-52fb2010b7be.json'

storage_credentials= service_account.Credentials.from_service_account_file(path_to_token)
storage_client = storage.Client(project=project_id, credentials = storage_credentials)

#Destination

destination_bucket_name = "food_recommendation"
destination_bucket = storage_client.bucket(destination_bucket_name)


destination_blob_name = 'export_dataframe.csv'
blob = destination_bucket.blob(destination_blob_name)


source_file_name = "export_dataframe.csv"
blob.upload_from_filename('export_dataframe.csv')