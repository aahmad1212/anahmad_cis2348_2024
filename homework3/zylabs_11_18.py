# Adil Ahmad
# 2278219
nums = input().split()
numlist = list(map(int, nums))
for i in numlist[:]:
    if i < 0:
        numlist.remove(i)
numlist.sort()
for i in numlist:
    print(i, end=" ")
