# Rayyan Rahman ID: 1893113

def get_age():          #gets user input and checks to see if valid age range
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age


def fat_burning_heart_rate(age):   #calc heart rate with given user input(age)
    heart_rate = (220 - age) * .70
    return heart_rate

if __name__ == "__main__":

    try:
        age = get_age()         #calls def get_age and fat_burning_heart_rate
        bpm = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a', age, 'year-old:', bpm, 'bpm')
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')