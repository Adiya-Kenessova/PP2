#RegEx (Regular expression) can be used to check if a string contains the specified search pattern

#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")                  #YES! We have a match!


#Return a list containing every occurrence of "ai":
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)                            #['ai', 'ai']

#ex/ Search for the first white-space character in the string
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) #The first white-space character is located in position: 3
#Note: If there is no match, the value None will be returned, instead of the Match Object.

#Split at each white-space character:
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)                              #['The', 'rain', 'in', 'Spain']

#Split the string at the first white-space character:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)                              #['The', 'rain in Spain']

#Replace all white-space characters with the digit "9":
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)                            #The9rain9in9Spain


#Search for an upper case "S" character in the beginning of a word, and print its position:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())                        #(12, 17)

#The string property returns the search string:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)                        #The rain in Spain

#Search for an upper case "S" character in the beginning of a word, and print the word:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())                        #Spain






