import os
import shutil

# Put your folder paths here
folder_a = "Downloads/Old_Photos"
folder_b = "Desktop/Jpg_Files"

def start_moving():
    # making the folder if it's not there
    if not os.path.exists(folder_b):
        os.makedirs(folder_b)
        print("Created new folder...")

    files = os.listdir(folder_a)
    count = 0

    for f in files:
        # checking for jpg files specifically
        if f.endswith(".jpg"):
            source = os.path.join(folder_a, f)
            destination = os.path.join(folder_b, f)
            
            shutil.move(source, destination)
            print("Moved:", f)
            count += 1

    print("Task done. Total files moved:", count)

start_moving()