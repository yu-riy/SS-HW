import os
from os import path
import time

user_name = input("Enter a username, please\n")
user_message = input(f"Leave your message, {user_name}\n")

fd = f"{user_name}.txt"

if path.exists(fd):
    current_file = open(fd, "a")

    current_file.write(f"{time.ctime()}\n")
    current_file.write(f"{user_message}\n")
    current_file.close()
else:
    current_file = open(fd, "w")
    current_file.write(f"{user_name}\n")
    current_file.write(f"{time.ctime()}\n")
    current_file.write(f"{user_message}\n")
    current_file.close()




