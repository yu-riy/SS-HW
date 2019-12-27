# Task 2. DNA

import string

valid_chars = ("A", "C", "T", "G")
input_chars = "ACTG"
output_chars = "TGAC"

def trans_string():

    while True:
        user_string = input("Please enter the string: \n")
        if not user_string:
            continue
        if set(user_string).issubset(valid_chars):
            break
    trans_table = user_string.maketrans(input_chars, output_chars)
    answear = user_string.translate(trans_table)

    print(f"\nOriginal string is {user_string}")
    print(f"\nConverted string is {answear}")
            
trans_string()
