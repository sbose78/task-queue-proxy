from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

from jobs.utils import trigger_gcm_request,run_sql
from jobs import rules 

########### Sample tasks to test the framework ############################

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def check(a):
	return a

############# Sample tasks end here, real tasks start here ################

@shared_task
def send_gcm_notification(REG_ID_LIST=None,_data=None):
	import json


	result = trigger_gcm_request(API_KEY = None , REG_ID = [ REG_ID_LIST ] , data = _data)  
	# The method is configured to use default values.
	# In prod, the above method would need arguments namely
	# REG_ID , data 

	print result
	if 'errors' in result:
		print "will take out erroneous GCM IDs and execute again for the failed transactions"
		# Queue up more tasks.

	print "Successfuly sent out notif"
	return result	

@shared_task
def send_email( subject , body , to , sender ) :
	return True


@shared_task
def validate_policy( policy ):
	result,reason = rules.validate_policy( policy ) 
	return { "result": result , "error" : reason }


@shared_task
def execute_policy( policy ):
	response = {}
	response["result"] = {}
	
	


'''
Defining signals here. This method will be called after a task is executed 
'''

from celery.signals import after_task_publish , task_postrun
from celery.signals import celeryd_init



@task_postrun.connect(sender=None)
def task_completed_handler(sender=None, **kwds ): #task_id=None ,  task=None, args=None,
                      #kwargs=None, **kwds  ):#retval=None , state=None, **kwargs):

    print "|||||||||||||||||||||||||| %s  %s"%( sender, sender.name )
    print("#$%$%#$%#$%######################## ",( sender , kwds  ))

    input = None
    ouput = None
    result = None
    celery_task_id = None

    result_dict = {}	
    for k,v in kwds.iteritems():
         print "%s = %s" % (k, v)
	 result_dict[k] = v

    sql = 'INSERT INTO `task_status` (`task_name`, `input`, `output`, `celery_task_id` , `type` ) VALUES ("daily_recommendation", "%s", "%s", "%s","%s");'%(result_dict['args'], result_dict['retval'], result_dict['task_id'] , sender.name)
    run_sql(sql)  

    print "End of task, exeuting %s for task logging"%(sql)
	 
    

print "Tasks module initiated"

