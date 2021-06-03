# Worth per Seconds Calculator

print("\t\t******************************************")
print("\t\t* Welcome To Financial Worth Calculator. *\n")
print("\t\t******************************************")

print("\t\t1. Calculate worth per second based on a standard monthly wage.")
print("\t\t2. Calculate worth per second based on a standard weekly wage pay.")
print("\t\t3. Calculate worth per second based on a standard per hour basis.\n")


option = int(input("What Do You Wanna Calculate?\n "))



if option == 1:
	wageMonthly = float(input("How much do you earn per month(₦):\n "))
	daily = wageMonthly/20
	hourly = daily/12
	minutes = hourly/60
	seconds = minutes/60

	print("₦ per day: ₦",daily,"\n","₦ per hour: ₦",hourly,"\n","₦ per minute: ₦",minutes,"\n","₦ per second: ₦",seconds,"\n")

elif option == 2:
	wageWeekly = float(input("How much do you earn per week(₦):\n "))
	daily = wageWeekly/5
	hourly = daily/12
	minutes = hourly/60
	seconds = minutes/60

	print("₦ per day: ₦",daily,"\n","₦ per hour: ₦",hourly,"\n","₦ per minute: ₦",minutes,"\n","₦ per second: ₦",seconds,"\n")	

elif option == 3:
	wageContract = float(input("How much do you charge per hour(₦):\n "))
	hours = int(input("How many hours do you work per day: \n"))
	days = int(input("How many days do you work per week: \n"))
	contractLength = int(input("How many months is this contract lasting: \n"))
	daily = wageContract * hours
	weekly = daily * 5
	monthly = weekly * 4
	minutes = wageContract/60
	seconds = minutes/60
	
	print("₦ per day: ₦",daily,"\n","₦ per week: ₦",weekly,"\n","₦ per month: ₦",monthly,"\n","₦ per minute: ₦",minutes,"\n","₦ per second: ₦",seconds,"\n")

else:
	print("INCORRECT CHOICE. ")
