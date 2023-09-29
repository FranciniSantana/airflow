## MÓDULOS

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup



## DAGS
dag = DAG('daggroup', description =  'Dag Group',
          schedule_interval = None, start_date=datetime(2023,3,5),
          catchup = False)

## Tasks
task1 = BashOperator(task_id = 'tsk1',bash_command = 'sleep 5', dag = dag)
task2 = BashOperator(task_id = 'tsk2',bash_command = 'sleep 5', dag = dag)
task3 = BashOperator(task_id = 'tsk3',bash_command = 'sleep 5', dag = dag)
task4 = BashOperator(task_id = 'tsk4',bash_command = 'sleep 5', dag = dag)
task5 = BashOperator(task_id = 'tsk5',bash_command = 'sleep 5', dag = dag)
task6 = BashOperator(task_id = 'tsk6',bash_command = 'sleep 5', dag = dag)

#criando um grupo de tasks
tks_group = TaskGroup('tks_group',dag =dag)


task7 = BashOperator(task_id = 'tsk7',bash_command = 'sleep 5', dag = dag, task_group = tks_group) #note o parametro task_group nas tarefas que quero agrupar
task8 = BashOperator(task_id = 'tsk8',bash_command = 'sleep 5', dag = dag, task_group = tks_group)
task9 = BashOperator(task_id = 'tsk9',bash_command = 'sleep 5', dag = dag, task_group = tks_group,
                     trigger_rule = 'one_failed') # criando um trigger na task 3 para ser executada se uma task falhar

## Ordem de precedência
task1 >> task2
task3 >> task4
[task2,task4] >> task5 >> task6 >> [task7, task8,task9]
