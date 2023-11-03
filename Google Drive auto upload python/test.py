import os

directory_path = r"C:\KRISH\Main Branch XD\websites\cuberto" 

for root, _, files in os.walk(directory_path):
        for file in files:
            print(file)