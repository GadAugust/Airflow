from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def greeting():
    print('Hi! Welcome to airflow tutorial')

default_args = {
    'owner': 'Gad_August',
    'depends_on_past': False,
    'start_date': datetime(year=2024, month=3, day=23),
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'first_demo_dag', 
    default_args=default_args,
    description='This is a simple dag to show airflow',
    schedule_interval='0 1,23 * * 1-5',  # Corrected cron syntax for Mon-Fri at 1:00 and 23:00
    catchup=False,
) as dag:
    # Defining the first task
    task1 = PythonOperator(
        task_id='Greeting',
        python_callable=greeting,
    )

    # Defining the second task
    task2 = BashOperator(
        task_id='delay',
        bash_command='sleep 5',
    )

    # Defining the third task
    task3 = BashOperator(
        task_id='check_on_student',
        bash_command='echo "How are you doing today?"',
    )

    # Setting dependencies
    task1 >> task2 >> task3

      
      