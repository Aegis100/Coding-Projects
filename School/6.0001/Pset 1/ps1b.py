## 6.0001 Pset 1: Part b
## Name: Dylan Walker
## Time Spent: 
## Collaborators: None

#######################################################################################
## Get user input for salary, savings_rate, house_cost and biannual_raise below ##
#######################################################################################
salary = float(input("What is your yearly salary? "))
savings_rate = float(input("In decimal form, what is your savings rate? "))
house_cost = float(input("How much does your house that you are buying cost? "))
biannual_raise = float(input("In decimal form, what is your biannual raise percentage? "))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
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