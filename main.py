import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*', '#', '+', '!', '$', '%', '&', '(', ')', ';', '|', '=']


# for simple password - e.g 4-letter , 3 - symbol,  2- number  : GfUH*/(23 - order not randomised

num_letter = int(input("Enter the number of the letter to be in your password: "))
num_symbols = int(input("Enter number of symbols to be in your password: "))
nr_numbers = int(input("How many number would you like: "))

rand_letter = random.choices(letters, k = num_letter)
rand_symbol = random.choices(symbols, k = num_symbols)
rand_number = random.choices(numbers, k = nr_numbers)

password = rand_letter + rand_symbol + rand_number

# ['r', 'B' , 'U', '3', '9', '/', '?']  - PASSWORD

generated_password = ""

# looping through the list of password
for each_value in password:
    generated_password = generated_password + each_value

print(f"Your generated password is: {generated_password}")


# Harder level of Generated password
password_list = rand_letter + rand_symbol + rand_number

random.shuffle(password_list)

harder_password = ""
for char_value in password_list:
    harder_password += char_value

print(f"Your hard / randomized password is: {harder_password}")

