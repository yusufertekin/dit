from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now() - timedelta(days=1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('dit', catchup=False, default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='import_countries',
    bash_command='python3 /code/manage.py import_countries',
    dag=dag)

t2 = BashOperator(
    task_id='import_territories',
    bash_command='python3 /code/manage.py import_territories',
    dag=dag)

# TODO: Improve by incremental insert
sql = ("DELETE FROM geography_countryterritory; "
       "INSERT INTO geography_countryterritory "
       "(country, citizen_names, start_date, end_date, name, official_name, territory, id)"
       "SELECT country, citizen_names, start_date, end_date, name, official_name, territory,"
       "(ROW_NUMBER() OVER (ORDER BY name)) as id "
       "FROM (SELECT country, citizen_names, start_date, end_date, name, official_name, NULL as territory from "
       "geography_country UNION ALL "
       "SELECT NULL as country, NULL as citizen_names, start_date, end_date, name, official_name, territory FROM "
       "geography_territory) tmp order by name;")

t3 = PostgresOperator(
    task_id='merge_tables',
    sql=sql,
    postgres_conn_id='postgres_django',
    dag=dag)

t3.set_upstream([t1, t2])
