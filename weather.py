import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# COMPLETE!
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# COMPLETE!
def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # print(f"iso_string: {iso_string}") #expected value
    provided_date = iso_string.split("T")[0]
    # print(f"provided_date: {provided_date}") #expected value
    date_format = "%Y-%m-%d"
    raw_date = datetime.strptime(provided_date, date_format)
    # print(f" raw_date: {raw_date}") #expected value
    date_conversion = (raw_date.strftime("%A %d %B %Y"))
    # print(f"date_conversion: {date_conversion}") #expected value
    return(date_conversion)
# print(convert_date("2021-10-01T07:00:00+08:00")) #expected value

# COMPLETE!
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_conversion = ((float(temp_in_farenheit) - 32)* 5/9)
    celcius = round(temp_conversion,1)
    return celcius

# COMPLETE!
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    convert_data = []
    for element in weather_data:
        convert_data.append(float(element))
    # print(f"convert_data: {convert_data}") #expected value
    # print(f"convert_data type: {type(convert_data [0])}") #expected value
    length_of_input= len(convert_data) 
    # print(f"length_of_input: {length_of_input}") #expected value
    sum_of_input = sum(convert_data)
    # print(f"fum_of_input: {sum_of_input}") #expected value
    mean = sum_of_input/length_of_input
    # print(f"mean: {mean}") #expected value
    return mean
# print(calculate_mean([49, 57, 56, 55, 53]))

# FIXME:
def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.
    
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    # with open("tests/data/example_two.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    my_list = []
    for line in reader:
        # if the list is blank....
        if line == None:
            next
        else:
            my_list.append([f"{line[0]}", int(line[1]), int(line[2])])
    return my_list

# COMPLETE!
def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    convert_data = []
    for element in weather_data:
        convert_data.append(float(element))
    min_value = min(convert_data, default=None)
    if min_value ==  None:
        return ()
    else:
        position = []
        for value in range(len(convert_data)):
            if convert_data[value] == min_value:
                position.append(value) 
        return (min_value, position[-1])

# COMPLETE!
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    convert_data = []
    for element in weather_data:
        convert_data.append(float(element))
    max_value = max(convert_data, default=None)
    if max_value ==  None:
        return ()
    else:
        position = []
        for value in range(len(convert_data)):
            if convert_data[value] == max_value:
                position.append(value) 
        return (max_value, position[-1])

# FIXME:
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

# FIXME:
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

