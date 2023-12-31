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
    provided_date = iso_string.split("T")[0]
    date_format = "%Y-%m-%d"
    raw_date = datetime.strptime(provided_date, date_format)
    date_conversion = (raw_date.strftime("%A %d %B %Y"))
    return(date_conversion)

# COMPLETE!
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # temp_conversion = ((float(temp_in_farenheit) - 32)* 5/9)
    # celcius = round(temp_conversion,1)

    temp_conversion = round(((float(temp_in_farenheit) - 32)* 5/9),1)
    
    return temp_conversion

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
    length_of_input= len(convert_data) 
    sum_of_input = sum(convert_data)
    mean = sum_of_input/length_of_input
    return mean

# COMPLETE! 
def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.
    
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        my_list = []
        for line in reader:
            if len(line)==0:
                continue
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

# COMPLETE!
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # variables
    date_input=[]
    low_input=[]
    high_input=[]
    c_low_input=[]
    c_high_input=[]
    date_text=[]
    
    # WORKING! run through data to split into seperate lists.
    for row in weather_data:
        date_input.append(row[0])
        low_input.append(row[1])
        high_input.append(row[2])
    
    # WORKING! convert temperatures into celcius
    for value in low_input:
        c_low_input.append(convert_f_to_c(value))
    
    for value in high_input:
        c_high_input.append(convert_f_to_c(value))
    
    # WORKING! find min temps 
    # min temp and position in list
    min_temp = find_min(c_low_input)
    
    # WORKING! find max temps 
    # max temp and position in list
    max_temp = find_max(c_high_input)
    
    # WORKING! find averages
    mean_low = round(calculate_mean(c_low_input), 1)
    mean_high = round(calculate_mean(c_high_input), 1)
    
    # WORKING! convert dates into text
    for value in date_input:
        date_text.append(convert_date(value))
    
    # WORKING! find date of min temp
    for date in date_text:
        if min_temp[1] == date_text.index(date):
            min_temp_date = date
    
    # WORKING! find date of max temp
    for date in date_text:
        if max_temp[1] == date_text.index(date):
            max_temp_date = date
    
    summary = (f"{len(weather_data)} Day Overview\n  The lowest temperature will be {format_temperature(min_temp[0])}, and will occur on {min_temp_date}.\n  The highest temperature will be {format_temperature(max_temp[0])}, and will occur on {max_temp_date}.\n  The average low this week is {format_temperature(mean_low)}.\n  The average high this week is {format_temperature(mean_high)}.\n")
    
    return summary

# COMPLETE!
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    summary = ""
    for data in weather_data:
        summary +=(
                f"---- {convert_date(data[0])} ----\n"
                f"  Minimum Temperature: {format_temperature(convert_f_to_c(data[1]))}\n"
                f"  Maximum Temperature: {format_temperature(convert_f_to_c(data[2]))}\n\n"
        )
    return summary
