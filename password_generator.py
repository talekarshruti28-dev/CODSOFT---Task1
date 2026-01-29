import random

size = int(input("How many characters do you want in your password?"))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

all_together = letters + numbers + symbols

my_password = ""

for i in range(size):
    char = random.choice(all_together)
    my_password = my_password  + char

print("Your new password is:")
print(my_password)