from google.cloud import bigquery

SERVICE_ACCESS_JSON = '/home/...../bigquery-demo-308819-96977b1b6c1e.json'

client = bigquery.Client.from_service_account_json(SERVICE_ACCESS_JSON)

query_req = """
            CREATE TABLE dataset_py.newtable
            (
            x INT64 OPTIONS (description="An optional Integer Field"),
            y STRUCT<
                a ARRAY<STRING> OPTIONS(description="A repeated STRING field"),
                b BOOL
            >
            )
            OPTIONS(
                expiration_timestamp=TIMESTAMP "2023-01-01 00:00:00 UTC",
                description="a table that expire in 2023",
                labels=[("org_unit", "development")]
            )
"""

query_job = client.query(query_req)

print(query_job)
print("script ran ...")
