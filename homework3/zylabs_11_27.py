# Adil Ahmad
# 2278219
jerseys = {}

for i in range(5):
    jersey_num = int(input(f"Enter player {i+1}'s jersey number:\n"))
    rating = int(input(f"Enter player {i+1}'s rating:\n"))
    jerseys[jersey_num] = rating
    print()


def print_roster():
    print("ROSTER")
    jersey_keys = list(jerseys.keys())
    jersey_keys.sort()
    for x in jersey_keys:
        print(f"Jersey number: {x}, Rating: {jerseys[x]}")


print_roster()
option = ""

while option != "q":
    print(
        "\nMENU\n"
        "a - Add player\n"
        "d - Remove player\n"
        "u - Update player rating\n"
        "r - Output players above a rating\n"
        "o - Output roster\n"
        "q - Quit\n"
    )
    option = str(input("Choose an option:\n"))
    if option == "o":
        print_roster()

    if option == "a":
        new_num = int(input("Enter a new player's jersey number:\n"))
        new_rating = int(input("Enter a new rating for player:\n"))
        jerseys[new_num] = new_rating

    if option == "d":
        num_to_del = int(input("Enter a jersey number:\n"))
        del jerseys[num_to_del]

    if option == "u":
        num_to_update = int(input("Enter a jersey number:\n"))
        updated_rating = int(input("Enter a new rating for player:\n"))
        jerseys[num_to_update] = updated_rating

    if option == "r":
        rating_to_check = int(input("Enter a rating:\n"))
        print(f"\nABOVE {rating_to_check}")
        new_jerseys = {}

        for i in jerseys:
            if jerseys[i] > rating_to_check:
                new_jerseys[i] = jerseys[i]

        new_jersey_keys = list(new_jerseys.keys())
        new_jersey_keys.sort()

        for b in new_jersey_keys:
            print(f"Jersey number: {b}, Rating: {new_jerseys[b]}")
