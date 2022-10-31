import os

# absolute path
file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(file_path)

# empty message
my_message = ""

# file path
file_name = os.path.join(BASE_DIR,"templates","email.txt")

with open(file_name, 'r') as f:
    my_message = f.read()


print(my_message.format(name="Nelson"))
