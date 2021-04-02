def part_b(salary, savings_rate, house_cost, biannual_raise):
	#########################################################################
	percent_down_payment = 0.15
	amount_saved = 0.0
	r = 0.05
	months = 0.0
	down_payment = percent_down_payment * house_cost
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	while amount_saved <= down_payment:
	    amount_saved += salary / 12 * savings_rate
	    amount_saved += amount_saved * (r / 12)
	    months += 1
	    if months % 6 == 0:
	        salary = salary * (1 + biannual_raise)
	#######################################################
	## Print out the number of months it would take here ##
	#######################################################
	print (months)
	return months