#Rayyan Rahman ID: 1893113
cups_lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
cups_water = float(input('Enter amount of water (in cups):\n'))
cups_agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
# input the number of servings the recipe yields
cups_serving = float(input('How many servings does this make?\n'))

# display the input values
print('\nLemonade ingredients - yields {:.2f} servings' .format(cups_serving))
print('{:.2f} cup(s) lemon juice'.format(cups_lemon_juice))
print('{:.2f} cup(s) water'.format(cups_water))
print('{:.2f} cup(s) agave nectar'.format(cups_agave_nectar))

# input the desired number of servings
cups_serving_needed = float(input('\nHow many servings would you like to make?\n'))

# calculate the amount of each ingredient needed for 1 cup
lemon_juice_for_one = cups_lemon_juice/cups_serving
water_for_one= cups_water/cups_serving
agave_nectar_for_one = cups_agave_nectar/cups_serving

# calculate the amounts of each ingredient needed for desired servings
cups_lemon_juice_needed = lemon_juice_for_one*cups_serving_needed
cups_water_needed = water_for_one*cups_serving_needed
cups_agave_nectar_needed = agave_nectar_for_one*cups_serving_needed

# display the calculated amount of ingredients
print('\nLemonade ingredients - yields {:.2f} servings'.format(cups_serving_needed))
print('{:.2f} cup(s) lemon juice'.format(cups_lemon_juice_needed))
print('{:.2f} cup(s) water'.format(cups_water_needed))
print('{:.2f} cup(s) agave nectar'.format(cups_agave_nectar_needed))

# convert the calculated amount from cups to gallons (16 cups = 1 gallon)
gallons_lemon_juice = cups_lemon_juice_needed/16
gallons_water = cups_water_needed/16
gallons_agave_nectar = cups_agave_nectar_needed/16

# display the amounts in gallons
print('\nLemonade ingredients - yields {:.2f} servings'.format(cups_serving_needed))
print('{:.2f} gallon(s) lemon juice'.format(gallons_lemon_juice))
print('{:.2f} gallon(s) water'.format(gallons_water))
print('{:.2f} gallon(s) agave nectar'.format(gallons_agave_nectar))