print("--- Area of a Circle ---")
wah = input("Please enter your radius: ")
while not wah.isdigit() and wah != "":
    wah = input("Invalid input, please try again: ")
wah = int(wah)

def bruh(h):
    return 3.14159*h*h

print("The area of the circle is:", bruh(wah))