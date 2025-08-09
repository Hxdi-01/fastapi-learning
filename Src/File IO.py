with open ("textfile.txt", "w") as f:                             # creating a file
    f.write ("This is the first line.\n")                         # writing in a file

with open ("textfile.txt", "r")as f:                              # Opening the file to read
    print("Reading the file...")
    print (f.read())                                              # Printing the contents
with open("textfile.txt" ,"a") as f:
    f.write("This is the second line.\n")
with open ("textfile.txt","r") as f:
    print()