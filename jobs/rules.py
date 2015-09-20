
TEST_POLICY = '( stage > 0 and average_temperature < 7 ) or ( stage > 2 and temperature < 6 ) , recommend CRITICAL'
TEST_POLICY_LIST = [

	" stage is 0 and daily_light_integral < 40 , recommend CRITICAL",
	"( stage > 0 and average_temperature < 7 ) or ( stage > 2 and temperature < 6 ) , recommend CRITICAL",
	" policy is stage_0_borderline  and ignore_count >= 1 ",

]

TEST_PLANT = 'brinjal'
TEST_ALLOWED_ATTRIBUTES  = {

	# smartpot-plant assignment specific
	"stage":"",
	"temperature":"",
	"average_temperature":"",
	"zone":"",
	"daily_light_integral":"",
	"moisture":"",
	"total_duration":"",
	

	# static plant info
	"preferred_location":"",
	"type":"",
	"subtype":"",
	"difficulty":"",
	"max_stages":"5",
	"policy":"",

	#universal
	"month":"",

	#policy specific
	"ignore_count":"",
	"stage_0_borderline":"",
	"stage_1_borderline":"",
	"stage_2_borderline":"",

	

}

TEST_ALLOWED_GRAMMER = {
	"is":"=="
}

def validate_policy( policy ) :
	'''
		1. check for identifiers.
		2. check whether a True false is returned.
		3. check whether recommendation is provided
	'''
	policy = " %s "% ( policy ) 
	policy = transform_to_math_expression( policy ) 
	
	result,reason  = check_identifiers( policy ) 
	if result == False:
		return result, reason
	
	result,reason = check_bipolarity( policy )
	
	print "***Is the policy  %s  valid ? %s , If No, Errors? %s "%( policy,result,reason ) 
	return result,reason



def evaluate_policy( policy, plant ):
	'''
		1. Validate policy.
		2. Execute policy.
		3. return True if all OK , else False if policy is violated
	'''

######### checks ###############
def transform_to_math_expression( _policy ):
	global TEST_ALLOWED_GRAMMER
	allowed_grammer = TEST_ALLOWED_GRAMMER

        for gr in allowed_grammer :
                _policy = _policy.replace(" %s "%( gr ) , ' %s '%( allowed_grammer[gr] ) )
        print "After english to math op translations : %s "%( _policy )
	return _policy

	

def check_identifiers( policy ):
	global TEST_ALLOWED_ATTRIBUTES,TEST_ALLOWED_ATTRIBUTES

	_policy = policy.split(",")[0] # copying for modifications
	identifier_list = TEST_ALLOWED_ATTRIBUTES

	for i in identifier_list :
		_policy = _policy.replace( " %s "%(i) , ' 1 ')

	print "After id replacement : %s"%( _policy ) 
	

	allowed_operators =  ['>=','<=','==','>','<','and' , 'or']
	for op in allowed_operators :
		_policy = _policy.replace( " %s "%(op) , ' + ') 

	print "After policy replacement : %s"%( _policy )
	
	try:
		print "Evaluating value... %s"% ( eval( _policy ) )
	
	except Exception as e:
		print "Invalid variables found %s"%( e )
		return False,e

	return True,''


def check_bipolarity( policy ) :
	global TEST_ALLOWED_ATTRIBUTES

	pre,reason = check_identifiers( policy )
	if pre == False :
		return False,reason

        _policy = policy.split(",")[0] # copying for modifications
        identifier_list = TEST_ALLOWED_ATTRIBUTES

        for i in identifier_list :
                _policy = _policy.replace( " %s "%(i) , ' 1 ')

        print "After id replacement : %s"%( _policy )
     
        try:
                print "Evaluating value... %s"% ( eval( _policy ) )

        except Exception as e:
                print "Invalid variables found %s"%( e )
                return False,e

        return True,''

 
if __name__ == "__main__":
	global TEST_POLICY, TEST_POLICY_LIST
	#print check_bipolarity( TEST_POLICY )

	for policy in TEST_POLICY_LIST :
		validate_policy( policy )

 

			 

