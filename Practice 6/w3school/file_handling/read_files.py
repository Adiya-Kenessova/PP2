'''"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists'''

#to open file:
f = open("demofile.txt")
#to read (get whats in file):
f = open("demofile.txt")          #or f = open("D:\\myfiles\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
  print(f.read())
#close file
f = open("demofile.txt")
print(f.readline())
f.close()

#read first 5 char:
with open("demofile.txt") as f:
  print(f.read(5))
