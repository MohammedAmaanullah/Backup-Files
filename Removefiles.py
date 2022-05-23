import os
import shutil
import time

path=input("Enter the directory you want to organize: ")
days=input("Enter the number of days: ")

seconds=time.time(days)
os.path.exists(path)