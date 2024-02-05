import secrets
import string

def generator(length):
    index = 0
    password = ""
    while index <= length:
        choice = secrets.choice(secrets.choice(collective))
        password += str(choice)
        index += 1
    return password

collective = [[x for x in range(10)],string.ascii_letters[0:int(len(string.ascii_letters)/2)],
              string.ascii_letters[int(len(string.ascii_letters)/2):],string.punctuation]

try:
    length = int(input("Enter length of password:\n"))
    if length < 5:
        print("Password should be atleast 5 characters long")
    else:
        print(f"Password:{generator(length)}")
except:
    print("Error: Wrong data type")