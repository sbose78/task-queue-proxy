from django.db import models

# Create your models here


from celery.signals import after_task_publish

@after_task_publish.connect( sender='jobs.tasks.mul' )
def task_sent_handler(sender=None, body=None, **kwargs):
    print('after_task_publish for task id {body[id]}'.format(
        body=body,
    ))

print "This works here"


