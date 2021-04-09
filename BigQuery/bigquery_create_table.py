from google.cloud import bigquery

service_account_json = r'/home/i-sip_iot/PycharmProjects/bigquery-demo-308819-96977b1b6c1e.json'

# construct a bigquery client object
client = bigquery.Client.from_service_account_json(service_account_json)

# Set table id to the ID of the table to create
table_id = "bigquery-demo-308819.dataset_py.table_py"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("gender", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("count", "INTEGER", mode="NULLABLE")
    ],
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1
)

file_path = r'/home/i-sip_iot/Downloads/yob1880.txt'

source_file = open(file_path, 'rb')

job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()    # waits for the job to complete

table = client.get_table(table_id)

print(
    "Load {} rows in {}".format(table.num_rows, table_id)
)