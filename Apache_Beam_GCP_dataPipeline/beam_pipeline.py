import apache_beam as beam
# import the packages PipelineOptions and StandardOptions for standard configurations like executing the pipeline
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import argparse
from google.cloud import bigquery

# project-id:dataset_id.table_id
delivered_table_spec = 'bigquery-demo-308819:dataset_food_orders_latest.delivered_orders'
other_table_spec = 'bigquery-demo-308819:dataset_food_orders_latest.other_status_orders'
# ######################## Mandatory Part to run any Beam pipeline ########################################
parser = argparse.ArgumentParser()

parser.add_argument('--input', dest='input', required=True, help='input file to process.')

# pipeline_args will hold the environmental args and path_args will hold the import file location
path_args, pipeline_args = parser.parse_known_args()


input_pattern = path_args.input
options = PipelineOptions(pipeline_args)

p = beam.Pipeline(options=options)
############################################################################################################


def remove_last_colon(row):
    """
    a method which is used in Map transformation. Map basically applies a simple one to one mapping function over each
    element in the collection. It means it just receive one row and its output is just one row. This function will
    split each row based on , and then remove the : and join the material again
    :param row:
    :return:
    """
    cols = row.split(',')
    item = str(cols[4])

    if item.endswith(':'):
        cols[4] = item[:-1]

    return ','.join(cols)


def remove_special_characters(row):
    """
    remove the special characters from the rows
    :param row:
    :return:
    """
    import re
    cols = row.split(',')
    ret = ''
    for col in cols:
        clean_col = re.sub(r'[?%&]', '', col)
        ret = ret + clean_col + ','
    ret = ret[:-1]
    return ret


def print_row(row):
    print(row)

# Write Transformation to clean the data in beam
# p collection is a unified storage of beam that store any batch or streaming data
cleaned_data = (
    p
    | beam.io.ReadFromText(input_pattern, skip_header_lines=1)
    | beam.Map(remove_last_colon)     # Map applies a simple one to one mapping func over each element in the collection
    | beam.Map(lambda row: row.lower())
    | beam.Map(remove_special_characters)
    | beam.Map(lambda row: row + ',1')
)
# Now wee need to write the deliver status item in one table and the rest in another table
# so we need to store these two types of the data into two p collections, the first would be delivered_orders
# You can provide a unique label to any p transform, you cannot use two transformation in same code without providing
# any unique label to it
delivered_orders = (
    cleaned_data
    | 'delivered filter' >> beam.Filter(lambda row: row.split(',')[8].lower() == 'delivered')
)
other_orders = (
    cleaned_data
    | 'undelivered filter' >> beam.Filter(lambda row: row.split(',')[8].lower() != 'delivered')
)

(cleaned_data
 | 'count table' >> beam.combiners.Count.Globally()
 | 'total map' >> beam.Map(lambda x: 'Total Count:' + str(x))   # Total Count: 900
 | 'print total' >> beam.Map(print_row)
)

(delivered_orders
 | 'count delivered' >> beam.combiners.Count.Globally()
 | 'delivered map' >> beam.Map(lambda x: 'Total Count:' + str(x))
 | 'print delivered count' >> beam.Map(print_row)
)

(other_orders
 | 'count others' >> beam.combiners.Count.Globally()
 | 'other map' >> beam.Map(lambda x: 'Total Count:' + str(x))
 | 'print other count' >> beam.Map(print_row)
)

service_account_json = r'/home/i-sip_iot/PycharmProjects/bigquery-demo-308819-96977b1b6c1e.json'

client = bigquery.Client.from_service_account_json(service_account_json)

dataset_id = "bigquery-demo-308819.dataset_py"

# if the dataset is available do not create it, else create the dataset
try:
    client.get_dataset(dataset_id)
except:
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset.description = "Dataset for food orders"
    dataset_ref = client.create_dataset(dataset, timeout=30)   # Making an API request

# Beam has a library to create and load data into BigQuery tables, by using Beam io package, WriteToBigQuery transform
# can be called. This command can create a table into bigquery while loading a p collection in it. It takes table_name,
# its schema, create_deposition and some additional things like partitioning and clustering as parameters.This transform
# takes input as json while the p collection we have now is in csv format and json conversion is needed.


def to_json(csv_str):
    fields = csv_str.split(',')

    json_str = {"customer_id": fields[0],
                "date": fields[1],
                "timestamp": fields[2],
                "order_id": fields[3],
                "items": fields[4],
                "amount": fields[5],
                "mode": fields[6],
                "restaurant": fields[7],
                "status": fields[8],
                "ratings": fields[9],
                "feedback": fields[10],
                "new_col": fields[11]
                }

    return json_str


table_schema = 'customer_id:STRING,date:STRING,timestamp:STRING,order_id:STRING,items:STRING,amount:STRING,' \
               'mode:STRING,restaurant:STRING,status:STRING,ratings:STRING,feedback:STRING,new_col:STRING'

(delivered_orders
 | 'delivered to json' >> beam.Map(to_json)
 | 'write delivered' >> beam.io.WriteToBigQuery(
            delivered_table_spec,
            schema=table_schema,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            additional_bq_parameters={'timePartitioning': {'type': 'DAY'}}
        )
 )

(other_orders
 | 'other to json' >> beam.Map(to_json)
 | 'write other_orders' >> beam.io.WriteToBigQuery(
            other_table_spec,
            schema=table_schema,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            additional_bq_parameters={'timePartitioning': {'type': 'DAY'}}
        )
 )


from apache_beam.runners.runner import PipelineState
ret = p.run()
if ret.state == PipelineState.DONE:
    print('Success!!!')
else:
    print('Error Running beam pipeline')


view_id = "bigquery-demo-308819.dataset_food_orders_latest.daily_food_orders"
view = bigquery.Table(view_id)

# The source table in this example is created from a CSV file in Google
# Cloud Storage located at
# `gs://cloud-samples-data/bigquery/us-states/us-states.csv`. It contains
# 50 US states, while the view returns only those states with names
# starting with the letter 'W'.
# view.view_query = f"SELECT * FROM `{source_id}` WHERE _PARTITIONDATE = DATE(current_date ())"
view.view_query = 'select * from `bigquery-demo-308819.dataset_food_orders_latest.delivered_orders` ' \
                  'where _PARTITIONDATE = DATE(current_date ())'

# Make an API request to create the view.
try:
    view = client.create_table(view)
    print(f"Created {view.table_type}: {str(view.reference)}")

except:
    print('view already exists')
