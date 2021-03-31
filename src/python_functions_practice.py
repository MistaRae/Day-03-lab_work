def return_10():
    return 10
    
def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month):
    list_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month -= 1
    return list_months[month]

def number_to_short_month_name(month):
    list_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month -= 1
    return list_months[month]

def cube_this(dimension):
    return dimension ** 3

def reverse_string(string_to_be_reversed):
    return string_to_be_reversed[::-1]

def farenheit_to_celsius(far_input):
    return round(((far_input - 32) * 5 / 9), 4)