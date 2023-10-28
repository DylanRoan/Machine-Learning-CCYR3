print("--- Minutes Into Seconds ---")
val = input("Please enter your minutes: ")
while not val.isdigit() and val != "":
    val = input("Invalid input, please try again: ")
val = int(val)

def fun(m): 
    return m*60

print(val,"minutes is",fun(val),"seconds!!!")