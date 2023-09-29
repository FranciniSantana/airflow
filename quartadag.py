## MÓDULOS

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime



## DAGS EM CONTEXTO COM WITH AS
with DAG('quarta_dag', description =  'Nossa quarta DAG',
          schedule_interval = None, start_date=datetime(2023,3,5),
          catchup = False) as dag:

    ## Tasks
    task1 = BashOperator(task_id = 'tsk1',bash_command = 'sleep 5')
    task2 = BashOperator(task_id = 'tsk2',bash_command = 'sleep 5')
    task3 = BashOperator(task_id = 'tsk3',bash_command = 'sleep 5')

    ## Ordem de precedência usando função em vez de bitwise
    task1.set_upstream(task2)
    task2.set_upstream(task3)
