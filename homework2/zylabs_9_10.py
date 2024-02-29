# Adil Ahmad
# 2278219
import csv

inputcsv = str(input())
with open(inputcsv, "r") as csvfile:
    input_reader = csv.reader(csvfile)
    for row in input_reader:
        wordlist = row

unique_list = list(dict.fromkeys(wordlist))
length = len(unique_list)
for i in range(length):
    print(unique_list[i], wordlist.count(unique_list[i]))
