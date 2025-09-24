import os
import random
import string

filename = input("password list file name (without .txt): ") + ".txt"

# i hope this makes it work on anything
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

filepath = os.path.join(desktop, filename)

num_passwords = int(input("How many password to gen?: "))

password_length = int(input("How long each password?:"))

characters = string.ascii_letters + string.digits + string.punctuation

# create and write
with open(filepath, "w") as f:
    for i in range(num_passwords):
        password = "".join(random.choice(characters) for _ in range(password_length))
        f.write(password + "\n")

print(f"list saved as {filepath}")
