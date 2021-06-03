salary = float(input("enter salary for month: "))
transportWork = float(input("enter transportWork each day: "))
transportChurch = float(input("enter transportChurch each week: "))
feeding = float(input("enter feeding each day: "))
tithe = salary/10
offering = float(input("enter offering each week: "))
debt = float(input("enter debt for month: "))

transportWorkWeek = transportWork * 5
transportWorkMonth = transportWorkWeek * 4
transportChurchMonth = transportChurch * 4
feedingWeek = feeding * 5
feedingMonth = feedingWeek * 4
offeringMonth = offering * 4

budgetWeek = transportWorkWeek + feedingWeek + offering
budgetMonth = transportWorkMonth + transportChurchMonth + feedingMonth + offeringMonth + tithe + debt
balance = salary - budgetMonth

print('Your details: Salary: ',salary,'\n Work TP: ',transportWorkMonth,'\n Feed: ',feedingMonth,'\n Tithe & Offering: ',tithe+offeringMonth,'\n Church TP: ',transportChurchMonth,'\n Total Budget Per Week: ',budgetWeek,'\n Total Budget Per Month: ',budgetMonth,'\n Balance: ',balance)
