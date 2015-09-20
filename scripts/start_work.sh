#celery -A http_task_gateway worker -l info
celery multi start 1 -A  http_task_gateway -l info 
