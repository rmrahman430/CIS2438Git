# Rayyan Rahman ID: 1893113

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
