print("--- Odd or Even ---")
wah = input("Please enter your number: ")
while not wah.isdigit() and wah != "":
    wah = input("Invalid input, please try again: ")
wah = int(wah)

print("Your number is", "EVEN" if wah % 2 == 0 else "ODD")