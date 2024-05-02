# Adil Ahmad
# 2278219
def get_age():
    y = int(input())
    if y <= 18 or y >= 75:
        raise ValueError("Invalid age.")
    return y


def fat_burning_heart_rate(x):
    heart_rate = (220 - x) * 0.7
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
    except ValueError as excpt:
        print(f"{excpt}\nCould not calculate heart rate info.\n")
    else:
        print(f"Fat burning heart rate for a {age} year-old: {fat_burning_heart_rate(age)} bpm")
