income = int(input("enter the income: "))

tax = 0 

if income>=250000 and income<=500000:
    tax = 0.05*income 
elif income>=500000 and income<=750000:
    tax = 0.10*income
elif income>=750000 and income<=1000000:
    tax = 0.15*income
elif income>=1000000 and income<=1250000:
    tax = 0.20*income
elif income>=1250000 and income<=1500000:
    tax = 0.25*income
elif income>=1500000:
    tax = 0.30*income
else:
    print("tax relaxation")

print("tax amount: ", tax)

