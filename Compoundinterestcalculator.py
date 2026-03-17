principal = 0
rate = 0
time = 0 # Time in years

while principal <= 0:
    principal = float(input("Enter the principle amount: "))
    if principal <= 0:
        print("Principal can't be lower or equal to 0")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be lower or equal to 0")

while time <= 0:
    time = int(input("Enter the amount of years: "))
    if time <= 0:
        print("Time can't be lower or equal to 0")

total = principal * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")