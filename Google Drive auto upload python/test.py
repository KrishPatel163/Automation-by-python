import os

directory_path = r"C:\KRISH\Main Branch XD\Pyhton\Google Calendar API" 

for root, _, files in os.walk(directory_path):
        for file in files:
            print(file)