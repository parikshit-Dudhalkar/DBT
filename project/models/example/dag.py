# import yaml

# file_path='/workspaces/DBT/project/models/example/my_first_dbt_model.yml'


# with open(file_path,"r") as file:
#     config=yaml.safe_load(file)

# print(config)




# /path/to/your/airflow/dags/dbt_dag.py

import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define your virtual environment and dbt project directory paths
VENV_PATH = r"E:\dbt\dbt_Env\Scripts\activate.bat" 


 # Path to your virtualenv
DBT_PROJECT_PATH = r"E:\dbt\dbt_proj"  # Path to your dbt project

# Define your Airflow DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2024, 11, 21),  # Adjust this date as needed
}

with DAG('dbt_run_dag',
         default_args=default_args,
         schedule_interval='@daily',  # Set the schedule interval for running dbt
         catchup=False) as dag:

    # Activate the virtual environment and run dbt command
    dbt_run = BashOperator(
        task_id='run_dbt',
        bash_command=f"source {VENV_PATH} && cd {DBT_PROJECT_PATH} && dbt run -m airbnbfirst",  # Change 'dbt run' to your specific dbt command
    )

    # Set the task dependencies (if you have more tasks, you can chain them here)
    dbt_run
