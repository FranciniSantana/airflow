## MÓDULOS

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime



## DAGS
dag = DAG('segunda_dag', description =  'Nossa segunda DAG',
          schedule_interval = None, start_date=datetime(2023,3,5),
          catchup = False)

## Tasks
task1 = BashOperator(task_id = 'tsk1',bash_command = 'sleep 5', dag = dag)
task2 = BashOperator(task_id = 'tsk2',bash_command = 'sleep 5', dag = dag)
task3 = BashOperator(task_id = 'tsk3',bash_command = 'sleep 5', dag = dag)

## Ordem de precedência executando primeiro a task 1 e a task 2 e três em seguida e em paralelo
task1 >> [task2, task3]