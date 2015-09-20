
a=0

while [ $a -le 1 ]
do
   echo $a
   a=`expr $a + 1`
#   curl -X POST -d '{"args":[ "APA91bH_s8KxnQmUuDOjKkE1mNcV2f2Fx9bcZScvhHg06BjHAlDYRqN5hvwfdo0lFTNdlcE2U4XGhwzd1MKjxopiI8_DOlnSztWGXFaL3sNtNxa7pkHOTxYYsHmDKz07wrh6ZI8iPv5o", {"the_message":"dsfjsfs" , "param2":"var2" }  ]}' http://localhost:5555/api/task/async-apply/jobs.tasks.send_gcm_notification
   curl -X POST -d '{"args":[ " stage is 0 and daily_light_integral < 40 , recommend CRITICAL " ]}' http://localhost:5555/api/task/apply/jobs.tasks.validate_policy
done
