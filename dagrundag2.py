## MÓDULOS

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime



## DAGS
dag = DAG('dagrundag2', description =  'Dag Run Dag 2',
          schedule_interval = None, start_date=datetime(2023,3,5),
          catchup = False)

## Tasks
task1 = BashOperator(task_id = 'tsk1',bash_command = 'sleep 5', dag = dag)
task2 = BashOperator(task_id = 'tsk2',bash_command = 'sleep 5', dag = dag)


## Ordem de precedência
task1 >> task2
