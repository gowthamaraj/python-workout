'''
 write a function, get_rainfall, that tracks rainfall in a number of cities. Users of your program will enter the name of a city; if the city name is blank, then
the function prints a report (which I’ll describe) before exiting.


 If the city name isn’t blank, then the program should also ask the user how much
rain has fallen in that city (typically measured in millimeters). After the user enters
the quantity of rain, the program again asks them for a city name, rainfall amount,
and so on—until the user presses Enter instead of typing the name of a city.
 When the user enters a blank city name, the program exits—but first, it reports
how much total rainfall there was in each city.
'''

from collections import defaultdict
rainfall = defaultdict(int)

def get_rainfall():
    while True:
        input_name = input('Enter City Name: ')
        if not input_name:
            break

        rain = int(input('Enter the Rain Amount: '))
        rainfall[input_name] += rain

    for city, rain in rainfall.items():
        print(f'{city} has {rain} rainfall')

get_rainfall()