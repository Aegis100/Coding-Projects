
import time

''' Programmed by Dylan Walker on 8/2/2020
Calculator '''

def addition(num1, num2):
    sumc = num1 + num2
    print (sumc)
    menu()

def subtraction(num1, num2):
    diff = num1 - num2
    print (diff)  
    menu()
    
def multiplication(num1, num2):
    product = num1 * num2
    print (product)
    menu()
    
def division(num1, num2):
    quotient = num1 / num2
    print (quotient)
    menu()
    
def exponent(num1, num2):
    exponential = num1 ** num2
    print (exponential)
    menu()

def operation(num1, num2):
    op = None
    while op == None:
        op = str(input("Please input your operation(+,-,*,**). "))
        if op == '+':
            addition(num1, num2)
        elif op == '-':
            subtraction(num1, num2)
        elif op == '*':
            multiplication(num1, num2)
        elif op == '**':
            exponent(num1, num2)
        else:
            print ("Operation not recognized. Try again.")
            op = None

def menu():
    try:
        num1 = int(input("Please input your first number. "))
        num2 = int(input("Please input your second number. ")) 
    except:
        print ("Your first or second inputs were not numbers. Try again.")
        menu()
    operation(num1, num2)
print ("Welcome to Dylan's calculator.")
menu()

