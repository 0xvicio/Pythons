from sys import argv
import time
import os

os.system('clear')

print ("Welcome to Rent Calculator")
print("==============================")
print("")
print("Today is:"), time.strftime("%m/%d/%y")
print("")

salary = 0
debt = 0
expenses = 0
rent = 0
total = 0
subtotal = 0
q = ""

print("To determine the elegibility for your dream house/apartment, you need to provide the following information")
print("Please, note that current rent information does not apply here.")
print("")


q = raw_input("This program will calculate your dream house. Would you like to continue?(y/n): ")

while (q == "yes") or (q == "y"):


	salary = input("Monthly Salary (after taxes): $")
	debt = input("How much do you spend on loans and credit cards: $")
	expenses = input("How much do you spend on food, clothes and other expenses?: $")
	rent = input("Please, enter rent amount of your dream house:$")


	total =  debt + expenses + rent
	subtotal = salary - total    

	print("Ater  expenses, dream house rent and debt, you will have:"), subtotal


	if subtotal < 0:
		print("")
	  	print("Oh man! You went way over your budget. Select a cheaper dream home or lay down on your expenses!")


	elif subtotal == 0:
		print("")
		print("Phew, that was close. You are at the edge. You might want to consider lay down on your expenses or select a different dream house.")

	elif subtotal > 0 and subtotal <=300:
		print ("")
		print("You will have enough money to survive, but you might want to lay down on your expenses.")

	else:
		if subtotal > 0 and subtotal > 300:
			print("")
			print("It looks like your calculations put you in a pretty stable state")


print("")
print("Thank you for using the Rent Calculator.")
