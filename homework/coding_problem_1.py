# Adil Ahmad
# 2278219
print("Age Calculator")
print('Enter the current date by month, day, and year.')
dmonth = int(input("Month: "))
dday = int(input("Day: "))
dyear = int(input("Year: "))

print('Enter your birthday by month, day, and year.')
bmonth = int(input("Month: "))
bday = int(input("Day: "))
byear = int(input("Year: "))

if (bmonth < dmonth) or (bmonth == dmonth and bday <= dday):
    age = dyear - byear
    print("You are", age, "years old.")
else:
    age = (dyear - 1) - byear
    print("You are", age, "years old.")
if bmonth == dmonth and bday == dday:
    print("Happy Birthday!")
