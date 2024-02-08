# Adil Ahmad
# 2278219
import math
hwall = int(input("Enter wall height (feet):\n"))
hwidth = int(input("Enter wall width (feet):\n"))
awall = hwall * hwidth
print("Wall area:", awall, "square feet")
paint = awall / 350
print(f"Paint needed: {paint:.2f} gallons")
print("Cans needed:", math.ceil(paint), "can(s)\n")
color = str(input("Choose a color to paint the wall:\n"))
colorprice = {
    "red": 35,
    "blue": 25,
    "green": 23
}
print("Cost of purchasing", color, "paint: $" + str((colorprice[color] * math.ceil(paint))))
