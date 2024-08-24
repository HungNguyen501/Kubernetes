"""Example bashoperator dag"""
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="example_dag",
    start_date=pendulum.datetime(2024, 8, 22, 0, 0, 0, tz="Asia/Ho_Chi_Minh"),
    schedule=None,
    catchup=False,
    max_active_tasks=1,
    max_active_runs=1,
    tags=["example",],
) as dag:
    hello_world_task = BashOperator(
        task_id='hello_task',
        bash_command='echo "Hello, this is an example."'
    )
