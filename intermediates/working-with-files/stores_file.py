import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_dir = os.path.join(BASE_DIR, 'images')

# if not os.path.exists(file_dir):
#     print("This is not a valid path")

os.makedirs(file_dir, exist_ok=True)

my_images = range(0,12)

# create multiple files on a fly
for i in my_images:
    file_name = f"{i}.txt"
    file_path = os.path.join(BASE_DIR, file_name) # absolute path

    # if path alredy exist
    if os.path.exists(file_path):
        print(f"Skipped {file_name}")
        continue

    # if not exist 
    with open(file_path, 'w') as f:
        f.write("Hello World")