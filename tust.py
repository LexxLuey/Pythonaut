feedingWeekDay = int(input("What is your budget for feeding in a single work day: N"))
transportWeekDay = int(input("What is your budget for transport in a single work day: N"))
transportSunday = int(input("What is your budget for transport in a single Sunday: N"))
offeringWeekly = int(input("What is your budget for offering in a week: N"))
familyMonth = int(input("What is your budget for family in a month: N"))
tithe = int(input("What is your budget for tithe in a month: N"))

transportWeekly = (transportWeekDay * 5) + transportSunday
feedingWeekly = feedingWeekDay * 5

offeringMonth = (offeringWeekly * 4) + tithe
transportMonth = transportWeekly * 4
feedingMonth = feedingWeekly * 4

print('\n')
print('Budget Per Week Feeding: N', feedingWeekly)
print('Budget Per Week Transport: N', transportWeekly)
print('Budget Per Week Offering & Tithe: N', offeringWeekly)
print('Budget Per Week Total: N', offeringWeekly+feedingWeekly+transportWeekly)

print('\n')
print('Budget Per Month Feeding: N', feedingMonth)
print('Budget Per Month Transport: N', transportMonth)
print('Budget Per Month Offering & Tithe: N', offeringMonth)
print('Budget Per Month Family: N', familyMonth)
print('Budget Per Month Total: N', familyMonth+offeringMonth+transportMonth+feedingMonth)
print('Savings Per Month: N', (55000-(familyMonth+offeringMonth+transportMonth+feedingMonth)))

print('\n')
print('Budget Per Year Feeding: N', feedingMonth*12)
print('Budget Per Year Transport: N', transportMonth*12)
print('Budget Per Year Offering & Tithe: N', offeringMonth*12)
print('Budget Per Year Family: N', familyMonth*12)
print('Budget Per Year Total: N', (familyMonth+offeringMonth+transportMonth+feedingMonth)*12)
print('Savings Per Year: N', (55000*12)-((familyMonth+offeringMonth+transportMonth+feedingMonth)*12))

feedingPercent = (feedingMonth/55000)*100.00
transportPercent = (transportMonth/55000)*100.00
offeringPercent = (offeringMonth/55000)*100.00
familyPercent = (familyMonth/55000)*100.00
savingsPercent = (((55000-(familyMonth+offeringMonth+transportMonth+feedingMonth)))/55000)*100.00

print('\n')
print('Feeding %:', feedingPercent)
print('Transporting %:', transportPercent)
print('Tithes and Offering %:', offeringPercent)
print('Family %:', familyPercent)
print('My balance %:', savingsPercent)
