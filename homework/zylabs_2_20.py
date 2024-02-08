# Adil Ahmad
# 2278219
juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n\n"))

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(nectar), 'cup(s) agave nectar\n')

desired_servings = float(input("How many servings would you like to make?\n\n"))
print('Lemonade ingredients - yields', '{:.2f}'.format(desired_servings), 'servings')
factor = desired_servings / servings
print('{:.2f}'.format(juice * factor), 'cup(s) lemon juice')
print('{:.2f}'.format(water * factor), 'cup(s) water')
print('{:.2f}'.format(nectar * factor), 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', '{:.2f}'.format(desired_servings), 'servings')
factor = desired_servings / servings
print('{:.2f}'.format((juice * factor) / 16), 'gallon(s) lemon juice')
print('{:.2f}'.format((water * factor) / 16), 'gallon(s) water')
print('{:.2f}'.format((nectar * factor) / 16), 'gallon(s) agave nectar')
