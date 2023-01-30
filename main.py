#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")
s=float(input("What was the total bill? $"))
tip=int(input("What percentage of tip would you like to give? 10,12,15? "))
people=int(input("How many people are going to split the bill? "))
tip_as=tip/100
total=s+(s*tip_as)
bill_per=total/people
final_Amt=round(bill_per,3)
print(f"Each person should pay: ${final_Amt}")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
