# Task 3. Shortest Word

def shortest_words():

    while True:
        user_string = input("Please enter the non-empty string: \n")
        if not user_string:
            continue
        else:
            break

    string_to_list = user_string.split()

    len_list = []
    for word in string_to_list:
        len_list.append(len(word))

   
    print(f"The length of the shortest word(s) is {min(len_list)}")
        
shortest_words()
