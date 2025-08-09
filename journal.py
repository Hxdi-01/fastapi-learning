with open ("journal.txt", "w", encoding ="utf-8") as file:
    file.write ("Today is the first day\n")

with open ("journal.txt", "a", encoding = "utf-8") as file:
    file.write("This is the second line\n")
    
with open ("journal.txt", "r", encoding = "utf-8") as file:
    print("Full content\n: ", file.read() )
    
with open ("journal.txt", "r", encoding = "utf-8") as file:
    for line in file:
        print("Line: ", line.strip())