from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from get_institutions import generate_institutions
from get_datax_enabled_institutions import get_datax_enabled_institutions
from check_report_to_run import check_attendance_plus_and_generate_reports, check_attendance_plus_and_generate_reports_fail
from check_reports_update import check_report1,check_report2,check_report3
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'datadrop',
    default_args=default_args,
    description='test DataDrop ETL process!',
    schedule_interval=timedelta(days=1),
)

#task_1
task_1 = PythonOperator(
    task_id='get_the_list_of_institutions_and_laconfig_details',
    python_callable=generate_institutions,
    dag=dag, 
)
#task_2
task_2 = PythonOperator(
    task_id='get_datax_enabled_institutions',
    python_callable=get_datax_enabled_institutions,
    dag=dag, 
)
#task_3
task_3 = PythonOperator(
    task_id='get_the_report_flags_and_generate_reports',
    python_callable=check_attendance_plus_and_generate_reports,
    dag=dag, 
)

#task_4
task_4 = PythonOperator(
    task_id='lastactivity_report',
    python_callable=check_report1,
    dag=dag, 
)
task_4.set_upstream(task_3)

#task_5
task_5 = PythonOperator(
    task_id='tlc_report',
    python_callable=check_report2,
    dag=dag, 
)
task_5.set_upstream(task_3)
#task_6
task_6 = PythonOperator(
    task_id='attendance_report',
    python_callable=check_report3,
    dag=dag, 
)
task_6.set_upstream(task_3)

task_1 >> task_2 >> task_3

##################################

dag_fail = DAG(
    'datadrop_failcase',
    default_args=default_args,
    description='test DataDrop fail ETL process!',
    schedule_interval=timedelta(days=1),
)

#task_1
task_1_fail = PythonOperator(
    task_id='get_the_list_of_institutions_and_laconfig_details',
    python_callable=generate_institutions,
    dag=dag_fail, 
)
#task_2
task_2_fail = PythonOperator(
    task_id='get_datax_enabled_institutions',
    python_callable=get_datax_enabled_institutions,
    dag=dag_fail, 
)
#task_3
task_3_fail = PythonOperator(
    task_id='get_the_report_flags_and_generate_reports',
    python_callable=check_attendance_plus_and_generate_reports_fail,
    dag=dag_fail, 
)

#task_4
task_4_fail = PythonOperator(
    task_id='lastactivity_report',
    python_callable=check_report1,
    dag=dag_fail, 
)
task_4_fail.set_upstream(task_3_fail)

#task_5
task_5_fail = PythonOperator(
    task_id='tlc_report',
    python_callable=check_report2,
    dag=dag_fail, 
)
task_5_fail.set_upstream(task_3_fail)
#task_6
task_6_fail = PythonOperator(
    task_id='attendance_report',
    python_callable=check_report3,
    dag=dag_fail, 
)
task_6_fail.set_upstream(task_3_fail)

task_1_fail >> task_2_fail >> task_3_fail