#function     Calculate an empoloyee's productivity bonus
#input        Interactive
#output       Employee name and bonus is printed

#declare and intitalize variables
Employee_Name = input("Enter employee's name: ")
numShifts = int(input("Enter Number of shifts:"))
numTrans = int(input("Enter Number of transactions:"))
dollarValue = float(input("Enter Transaction dollar value: "))


#calculate Productivity score
productivity_score = (float(dollarValue) // (numTrans) / numShifts)

#determine bonus
if productivity_score <= 30:
  Bonus = 50.00
else:
  if productivity_score <= 69:
    Bonus = 75.00
  else:
    if productivity_score <= 199:
      Bonus = 100.00
    else:
      Bonus = 200.00

#output employee name and bonus
print("Employee Name:", Employee_Name)
print("Employee bonus:", Bonus)
print("20240728_LeeAnthony_4-1")