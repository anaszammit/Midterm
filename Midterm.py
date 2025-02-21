#Q1
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a // 3)

#Q2
print(2+3*6/2)

#Q3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#Q4
def palindrome(word):
    word = str(word)
    if word == word[::-1]:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is NOT a palindrome.")


#Q5
def find_pattern(text):
    count = 0
    for i in range(len(text)):

        if text[i] == 'B' and text[i:].endswith("Bob"):
            count += 1
    return count


text = "bHelloBob bWorldBob bBob"
print(find_pattern(text))

#Q6
# Mutable List Example
my_list = [1, 2, 3]
print("Original List:", my_list)

# Modifying the list
my_list[0] = 10  # Changing an element
my_list.append(4)  # Adding an element
print("Modified List:", my_list)

# Immutable String Example
my_string = "hello"
print("Original String:", my_string)

# Attempting to modify the string (this will produce an error)
# my_string[0] = 'H'  # Uncommenting this line will raise a TypeError

# Creating a new string instead
new_string = "H" + my_string[1:]  # Replace 'h' with 'H'
print("New String:", new_string)


#Q7
import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Explanation: We will now process the list to remove odd numbers and double the even numbers.
# Create a new list to store the modified numbers
modified_numbers = []
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        modified_numbers.append(num * 2)  # Double the even number

# Replace the original list with the modified list
random_numbers = modified_numbers

# Print the final modified list
print(random_numbers)

#Q8
def is_valid_url(url):
    """
    Checks if the given parameter is a valid URL based on basic rules.

    :param url: The input string to check.
    :return: True if it's a valid URL, False otherwise.
    """
    # Check if it starts with "http://", "https://", or "www."
    if not (url[:7] == "http://" or url[:8] == "https://" or url[:4] == "www."):
        return False

    # Check if it contains at least one dot "." (domain part)
    if "." not in url:
        return False

    # Check if it contains spaces (invalid in URLs)
    for char in url:
        if char == " ":
            return False

    # Check if the input is an empty string
    if url == "":
        return False

    # If all conditions are met, it is a valid URL
    return True

# Test cases
print(is_valid_url("https://example.com"))  # True
print(is_valid_url(""))  # False

#Q9
def days_since_birth(birthday):
    # Parse the input date
    day, month, year = map(int, birthday.split('-'))

    # Define the current date manually
    current_day, current_month, current_year = 21, 2, 2025

    # Calculate the number of full years between the birth year and the current year
    full_years = current_year - year - 1

    # Calculate the total number of days excluding the birth year and the current year
    days_in_year = 365
    total_days = full_years * days_in_year

    return total_days

# Example usage
birthday = "13-04-2005"
days_passed = days_since_birth(birthday)
print(days_passed)










