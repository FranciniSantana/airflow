## MÓDULOS

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime



## DAGS
dag = DAG('triggerdag1', description =  'Nossa primeira trigger',
          schedule_interval = None, start_date=datetime(2023,3,5),
          catchup = False)

## Tasks
task1 = BashOperator(task_id = 'tsk1',bash_command = 'sleep 5', dag = dag)
task2 = BashOperator(task_id = 'tsk2',bash_command = 'sleep 5', dag = dag)
task3 = BashOperator(task_id = 'tsk3',bash_command = 'sleep 5', dag = dag,
                     trigger_rule = 'one_failed') # criando um trigger na task 3 para ser executada se uma falhar

## Ordem de precedência
[task1, task2] >> task3