# A function that returns the sun of two numbers
def add_numbers (num1, num2):
    num1 = 19
    num2 = 20
    return num1 + num2

# A function that returns an even number
def is_even (number):
    return number % 2 == 0

# A function that returns a reversed version of a string
def reverse_string(text):
    return text[::-1]

# A function that returns the count of vowels in a string
def count_vowels (text):
    text = "aEIou"
    return text

# A function that takes a non-negative integer n as input and returns the factorial of that number. 
def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

# Decorators
def apply_decorator (func):
    def wrapper():
        print("This function is about to be called")
        func()
    return wrapper
    
def decorator_func ():
    print("Decorator Applied")

decorator_func = apply_decorator(decorator_func)

# Sort List of Tuples
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

# Merge Dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Class creation
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print (f"Car Make: {self.make}, Car Model: {self.model}, Car Year: {self.year}")
