#To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("demofile.txt")

#check first if file exists
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.rmdir("myfolder")

#Note: You can only remove empty folders.
