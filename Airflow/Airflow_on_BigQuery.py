from airflow import models
from datetime import datetime, timedelta
from airflow.contrib.operators.dataflow_operator import DataFlowPythonOperator

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2020, 12, 24),
    'retries': 1,
    'retry_delay': timedelta(seconds=50),
    'dataflow_default_options': {
        'project': 'bigquery-demo-285417',
        'region': 'us-central1',
        'runner': 'DataflowRunner'
    }
}

with models.DAG('food_orders_dag',
                default_args=default_args,
                schedule_interval='@daily',
                catchup=False) as dag:
    t1 = DataFlowPythonOperator(
        task_id='beamtask',
        py_file='',
        options={'input': 'gs://daily_food_orders/food_daily.csv'}
    )
