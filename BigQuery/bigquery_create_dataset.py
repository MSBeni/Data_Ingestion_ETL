from google.cloud import bigquery

service_account_json = r'/home/.../bigquery-demo-308819-96977b1b6c1e.json'

client = bigquery.Client.from_service_account_json(service_account_json)

dataset_id = "bigquery-demo-308819.dataset_py"

dataset = bigquery.Dataset(dataset_id)

dataset.location = "US"
dataset.description = "Dataset from python"

dataset_ref = client.create_dataset(dataset, timeout=30)

print("Created Dataset {}.{}".format(client.project, dataset_ref.dataset_id))
