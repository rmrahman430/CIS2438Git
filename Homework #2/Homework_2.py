#Rayyan Rahman ID: 1893113
import datetime

with open("inputDates.txt", "r") as input_file, open("parsedDates.txt", "w") as output_file:
    for date_str in input_file:
        # Strip newline character
        date_str = date_str.strip()

        # Parse date
        try:
            date = datetime.datetime.strptime(date_str, "%B %d, %Y")
        except ValueError:
            # Ignore dates that don't match the format
            continue

        # Ignore dates that are later than current date
        if date > datetime.datetime.now():
            continue

        # Output date in desired format to console and file
        month = date.month
        day = date.day
        year = date.year
        output_str = f"{month}/{day}/{year}\n"
        print(output_str, end="")
        output_file.write(output_str)