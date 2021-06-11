# Meg Veitz
# 4/14/21
# Write a function that accepts two argumens: city name and country name.
# The function should return a single string of the form “City, Country” (Ex: Santiago, Chile).
# Store the function in a module (py file) called city_functions.py.
# Create a file called test_cities.py that tests the function you just wrote.


def combine_names(city_name, country_name):
    combined_names = "{}, {}".format(city_name, country_name)
    return combined_names
