import os
import time

directory = "C:\KRISH\Main Branch XD\Java\clg\Practical 3"

filesAndDirs = os.listdir(directory)

files = [f for f in filesAndDirs if os.path.isfile(os.path.join(directory,f))]

for file in files:
    if file.endswith(".class"):
        ToDelete = directory + "\\" + file
        print(f"File Deleted: {ToDelete}")
        os.remove(ToDelete)
        time.sleep(3)