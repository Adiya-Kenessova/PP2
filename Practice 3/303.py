
dict_str_int = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2", 
    "THR": "3",
    "FOU": "4",
    "FIV": "5", 
    "SIX": "6", 
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"}

dict_int_str = {
    "0": "ZER",
    "1": "ONE",
    "2": "TWO",
    "3": "THR",
    "4": "FOU",
    "5": "FIV",
    "6": "SIX",
    "7": "SEV",
    "8": "EIG",
    "9": "NIN"}
    
def str_to_int(tr_str):
    numm = ""
    i = 0
    while i < len(tr_str):
        triplet  = tr_str[i:i+3]
        numm += dict_str_int[triplet]
        i+=3
    return int(numm)

def int_to_str(tr_int):
    string1 = str(tr_int)
    num = ""
    i = 0
    while i < len(string1):
        num += dict_int_str[string1[i]]
        i+=1
    return num


s = input()
oper = None
for i in s:
    if i in "+-*":
        oper = i
        break
left, right = s.split(oper)

a = str_to_int(left)
b = str_to_int(right)
c = 0

if oper == "+":
    c = a+b
if oper == "-":
    c = a-b
if oper == "*":
    c = a*b

d = int_to_str(c)
print(d)
    





    