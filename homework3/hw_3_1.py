# Task 1. Count the number of Duplicates

def find_duplicates():
    user_string = input("Please enter the string which includes only alphabetic charactres\
or digits: \n")
    user_string.isalnum()
    user_str = user_string.lower()
    string_to_dict = dict.fromkeys(set(user_str.replace(" ", "")), 0)

    for char in user_str:
        if char in string_to_dict:
            string_to_dict[char] += 1
        else:
            continue
        
    answear = 0
    for char in string_to_dict:
        if string_to_dict[char] > 1:
            print (f"{char} occurs {string_to_dict[char]} times")
            answear += 1
    
    print(f"\n{answear} characters and numbers occur more than 1 time")

find_duplicates()
