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
