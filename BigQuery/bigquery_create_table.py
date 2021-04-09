from google.cloud import bigquery

service_account_json = r'/home/..../bigquery-demo-308819-96977b1b6c1e.json'

# construct a bigquery client object
client = bigquery.Client.from_service_account_json(service_account_json)

# Set table id to the ID of the table to create
table_id = "bigquery-demo-308819.dataset_py"

