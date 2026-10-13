from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="basic_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl"],
) as dag:

    extract_data = BashOperator(
        task_id="extract_data",
        bash_command='echo "Extracting data from source..."',
    )

    validate_data = BashOperator(
        task_id="validate_data",
        bash_command='echo "Validating extracted data..."',
    )

    transform_data = BashOperator(
        task_id="transform_data",
        bash_command='echo "Transforming data..."',
    )

    load_data = BashOperator(
        task_id="load_data",
        bash_command='echo "Loading data into warehouse..."',
    )

    send_notification = BashOperator(
        task_id="send_notification",
        bash_command='echo "Pipeline completed successfully!"',
    )

    # Task Dependencies
    extract_data >> validate_data >> transform_data >> load_data >> send_notification