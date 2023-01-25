#Rayyan Rahman ID: 1893113

print("Birthday Calculator")

print("Current day")

current_Month = int(input("Month: "))
current_Day = int(input("Day: "))
current_Year = int(input("Year: "))

print("Birthday")

Birth_Month = int(input("Month: "))
Birth_Day = int(input("Day: "))
Birth_Year = int(input("Year: "))

age = current_Year - Birth_Year - ((current_Month, current_Day) < (Birth_Month, Birth_Day))

print("You are", age, "years old.")

if (current_Month, current_Day) == (Birth_Month, Birth_Day):
    print("Happy Birthday!")
