# Reading and writing to files using python
import sys
import time

# Welcoming user
print("")
print("Welcome To Python File Reader and Writer.")
print("")

print("1. Read from File")
print("")
print("2. Add Data to File")
print("")
print("3. Write to New File")
print("")

option = input(str("Please Enter an Option :"))
print("")
option = int(option)

if option == 1:
    filename = input(str("Please Enter Filename :"))
    file = open(filename, "r")
    file = file.read()
    print("File Starts")
    print("")
    print(file)
    print("")
    print("File End.")

elif option == 2:
    print("")
    filename = input(str("Please Enter Filename : "))
    print("")
    filecontent = input(str("Please Enter Content for the File : "))
    print("")
    file = open(filename, "a")      # use 'a+' for append and write to file
    file.write("\n")
    file.write(filecontent)
    file.close()
    print("")
    print("File has been Saved.")

elif option == 3:
    print("")
    filename = input(str("Please Enter Filename : "))
    print("")
    filecontent = input(str("Please Enter Content for the File : "))
    print("")
    file = open(filename, "w")      # use 'w' for only writing to new file
    file.write("\n")
    file.write(filecontent)
    file.close()
    print("")
    print("File has been Saved.")

else:
    print("Please Enter a Valid Option..")
