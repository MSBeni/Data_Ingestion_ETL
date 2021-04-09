# README

Please first install the gcloud sdk using this command and this guide: https://cloud.google.com/sdk/docs/quickstart
```bash
sudo snap install google-cloud-sdk --classic
```

### Other useful commands:

```bash
bq show
bq show --dataset project_id:dataset_name
bq show --schema project_id:dataset_name.table_name
bq show --schema --format prettyjson dataset_name.table_name # Show in json format
bq ls  # list all datasets
bq ls dataset_name # list all table in that dataset
```

You acn always move to bq shell and remove the bq command and simply run through the shell

```shell
bq shell   # go to bigquery shell
```
and run all the above command without the ```bq``` command.
simply type ```exit``` to jump out of the shell.


### Having query in terminal using SDK:

```shell
bq query --use_legacy_sql=false 'SELECT * FROM project_id.dataset_name.table limit 10'

bq query --use_legacy_sql=false --label dummy_key1:value1 --label dummy_key2:value2 --batch=false --maximum_bytes_billed=30000000 --require_cache=false --destination_table=project_id.dataset_name.ney_dest_table --destination_schema name:string,gender:string,count:integer --time_partitioning_type=DAY --time_partitioning_expiration=90000 --clustering_fields=gender 'SELECT * FROM project_id.dataset_name.table limit 10'
```

### bq query flags
```shell
bq query \
--use_legacy_sql=false \
--append_table=false \
--destination_table \
--clustering_fields \
--batch=false \
--maximum_bytes_billed=30000000 \
--label key1:value1 \
--label key2:value2 \
--dry_run \    
'SELECT * FROM `bigquery-demo-285417`.dataset1.names limit 10'
```
with ```--dry_run``` flag, query will not be run and just the success message 
will be received in the case of successful query. Other examples are as follows:
```shell
bq query \
--use_legacy_sql=false \
--label dummy_key1:value1 \
--label dummy_key2:value2 \
--batch=false \
--maximum_bytes_billed=30000000 \
--require_cache=false \
--destination_table=bigquery-demo-285417:dataset1.names_ggg \
--destination_schema names:string,gend:string,count:integer \
--time_partitioning_field \
--clustering_fields=name \
--time_partitioning_expiration=90000 \
SELECT * FROM `bigquery-demo-285417.dataset1.names` limit 10
```


```shell
bq query --use_legacy_sql=false --label dummy_key1:value1 --label dummy_key2:value2 --batch=false --maximum_bytes_billed=30000000 --require_cache=false --destination_table=bigquery-demo-285417:dataset1.names_from_cli --destination_schema name:string,gender:string,count:integer --time_partitioning_type=DAY --time_partitioning_expiration=90000 --clustering_fields=gender "SELECT * FROM `bigquery-demo-285417.dataset1.names` limit 10"

bq mk --table --expiration 3000 --description "table from cli" --label dummy_key1:value1 --label dummy_key2:value2 --require_partition_filter --time_partitioning_type DAY --time_partitioning_expiration 4000 --clustering_fields name  --schema C:\Users\MyUser\Desktop\BQ_json_schema.txt dataset1.demo2

bq load bigquery-demo-285417:dataset1.names_from_cli C:\Users\MyUser\Desktop\yob1880.txt name:string,gender:string,count:integer
```

### Dataset Creation Command:
sample command:
```shell
bq mk --default_table_expiration 4000 -default_partition_expiration 5000 --description "new dataset" 'bigquery-demo-308819:dataset_bq'
```

