# Adil Ahmad
# 2278219
pass1 = str(input())
password = (
    pass1
    .replace("i", "!")
    .replace("a", "@")
    .replace("m", "M")
    .replace("B", "8")
    .replace("o", ".")
    + "q*s"
)
print(password)
