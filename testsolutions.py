import os

# Specify the path to your desktop (change this to your desktop path)
desktoppath = ()

# Initialize a dictionary to store file type counts
file_type_counts = {}

# Iterate through files on the desktop
for root, dirs, files in os.walk(desktoppath):
    for file_name in files:
        file_extension = file_name.split(".")[-1]
        if file_extension in file_type_counts:
            file_type_counts[file_extension] += 1
        else:
            file_type_counts[file_extension] = 1

# Print the counts of file types
for file_type, count in file_type_counts.items():
    print(f"File type: {file_type}, Count: {count}")