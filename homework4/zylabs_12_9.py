# Adil Ahmad
# 2278219

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        print(f"{name} 0")
    else:
        print(f'{name} {age}')
    finally:
        parts = input().split()
        name = parts[0]
