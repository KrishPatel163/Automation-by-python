import os
import re

# Define the directory where you want to search for the file.
search_directory = "C:\\Users\\krish\\Downloads"

# Define the regular expression pattern to match filenames.
pattern = r".*\{(.*)\}.*\{(.*)\}.*\{(.*)\}.*"

# List to store the found files.
found_files = []

# Compile the regular expression pattern for efficiency.
regex = re.compile(pattern)

for root, dirs, files in os.walk(search_directory):
    for filename in files:
        match = regex.match(filename)
        if match:
            # Extract the parameter values from the filename
            param1, param2, param3 = match.groups()
            cleaned_filename = filename.replace('{', '').replace('}', '')
            found_files.append((os.path.join(root, cleaned_filename), param1, param2, param3))

# Now, found_files contains tuples with the file path and extracted parameters.
for file_path, param1, param2, param3 in found_files:
    print("Found:", file_path)
    print("Param 1:", param1)
    print("Param 2:", param2)
    print("Param 3:", param3)
