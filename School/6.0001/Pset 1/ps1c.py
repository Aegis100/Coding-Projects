## 6.0001 Pset 1: Part c
## Name: Dylan Walker
## Time Spent: 1:30
## Collaborators: None

#############################################
## Get user input for initial_deposit below ##
#############################################
initial_deposit = float(input("What is your initial deposit? "))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months = 36
house_cost = 750000
down_payment = house_cost * .25
high_DP = down_payment + 100
low_DP = down_payment - 100
amount_saved = 0
high = 1
low = 0
steps = 0
########################################################################################################
## Determine the lowest return on investment needed to get the down payment for your dream home below ##
########################################################################################################
if initial_deposit > down_payment - 100:
    r = 0
else:
    while amount_saved - down_payment >= 100 or amount_saved - down_payment <= -100:
        r = (high + low) / 2
        amount_saved = initial_deposit * (1 + r / 12) ** months
        if amount_saved >= high_DP:
            high = r
        else:
            low = r
        if r >= .999:
            r = None
            break
        steps += 1
##########################################################
## Print out the best savings rate and steps taken here ##
##########################################################
print (r)
print (steps)