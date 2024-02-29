# Adil Ahmad
# 2278219
string = str(input())
newstring = string.replace(" ", "")
rstring = newstring[::-1]
if rstring == newstring:
    print(string + " is a palindrome")
else:
    print(string + " is not a palindrome")
