# Adil Ahmad
# 2278219
print(
    "Davy's auto shop services\n" +
    "Oil change -- $35\n" +
    "Tire rotation -- $19\n" +
    "Car wash -- $7\n" +
    "Car wax -- $12\n"
)
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}
service1 = input("Select first service:\n")
service2 = input("Select second service:\n")
print("\nDavy's auto shop invoice\n")
if service1 == "-" and service2 != "-":
    print("Service 1: No service")
    print("Service 2:", service2 + ", $" + str(services[service2]))
    print("\nTotal: $" + str(services[service2]))
elif service2 == "-" and service1 != "-":
    print("Service 1:", service1 + ", $" + str(services[service1]))
    print("Service 2: No service")
    print("\nTotal: $" + str(services[service1]))
elif service2 == "-" and service1 == "-":
    print("Service 1: No service")
    print("Service 2: No service")
    print("\nTotal: $0")
else:
    print("Service 1:", service1 + ", $" + str(services[service1]))
    print("Service 2:", service2 + ", $" + str(services[service2]))
    print("\nTotal: $" + str((services[service1] + services[service2])))
