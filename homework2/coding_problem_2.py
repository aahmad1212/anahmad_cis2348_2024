# Adil Ahmad
# 2278219
import datetime
validmonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
validdays = ["1,", "2,", "3,", "4,", "5,", "6,", "7,", "8,", "9,", "10,", "11,", "12,", "13,", "14,", "15,", "16,",
             "17,", "18,", "19,", "20,", "21,", "22,", "23,", "24,", "25,", "26,", "27,", "28,", "29,", "30,", "31,"]
validyears = str(range(0, 10000))
months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
today = datetime.date.today()
datetoday = today.strftime("%B %d, %Y")
datetoday_split = datetoday.split()
input_date = None
my_file = open("inputDates.txt", "r")
dates = my_file.readlines()
my_file2 = open("parsedDates.txt", "a")
for date in dates:
    input_date = date
    input_split = input_date.split()
    if input_date == "-1":
        continue
    if len(input_split) < 3:
        continue
    if input_split[0] not in validmonths and input_split[1] not in validdays and input_split[2] not in validyears:
        continue
    elif input_split[1] in validdays:
        input_split[1] = input_split[1].replace(",", "")
        datetoday_split[1] = datetoday_split[1].replace(",", "")
        if int(input_split[2]) <= int(datetoday_split[2]):
            if int(input_split[2]) == int(datetoday_split[2]):
                if months[input_split[0]] == months[datetoday_split[0]]:
                    if int(input_split[1]) <= int(input_split[1]):
                        output = str(months[input_split[0]]) + "/" + input_split[1] + "/" + input_split[2]
                        my_file2.write(output + "\n")
                        continue
                    else:
                        continue
                elif months[input_split[0]] > months[datetoday_split[0]]:
                    continue
                else:
                    output = str(months[input_split[0]]) + "/" + input_split[1] + "/" + input_split[2]
                    my_file2.write(output + "\n")
                    continue
            else:
                output = str(months[input_split[0]]) + "/" + input_split[1] + "/" + input_split[2]
                my_file2.write(output + "\n")
                continue
        else:
            continue
