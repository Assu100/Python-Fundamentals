# A function that returns the sun of two numbers
def add_numbers (num1, num2):
    print(num1 + num2)

add_numbers(10, 19)

# A function that returns an even number
def is_even (number):
    print(number % 2 == 0)

is_even(7)

# A function that returns a reversed version of a string
def reverse_string(text):
    print(text[::-1])

reverse_string("desk")

# A function that returns the count of vowels in a string
def count_vowels (text):
    vowels = "aeiou"
    text = text.lower()
    print(sum(1 for char in text if char in vowels))

count_vowels("happy")

# A function that takes a non-negative integer n as input and returns the factorial of that number. 
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)

calculate_factorial(10)

# Decorators
def apply_decorator (func):
    def wrapper():
        print("This function is about to be called")
        func()
    return wrapper
    
def decorator_func ():
    print("Decorator Applied")

decorator_func = apply_decorator(decorator_func)
decorator_func()

# Sort List of Tuples
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sort_by_age(people)

print(sorted_people)

# Merge Dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)

# Class creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print (f"Car Make: {self.make}, Car Model: {self.model}, Car Year: {self.year}")

car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2020)

car1.display_info()
print(car1)

car2.display_info()
print(car2)

