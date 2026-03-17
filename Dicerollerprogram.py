import random

# ● ┌ ─ ┐ │ └ ┘  This is to make the dice art, it usees code numbers to generate a specific "shape" for me

"┌──────────┐"
"│  ●    ●  │"
"│  ●    ●  │" # This dice art is important to make the dice art, time consuming to make tho
"│  ●    ●  │"
"└──────────┘"

dice_art = {
    1: ("┌──────────┐", 
        "│          │", 
        "│     ●    │", 
        "│          │", 
        "└──────────┘"),
    2: ("┌──────────┐", 
        "│   ●      │", 
        "│          │", 
        "│       ●  │", 
        "└──────────┘"),
    3: ("┌──────────┐", 
        "│     ●    │", 
        "│     ●    │", 
        "│     ●    │", 
        "└──────────┘"),
    4: ("┌──────────┐", 
        "│  ●    ●  │", 
        "│          │", 
        "│  ●    ●  │", 
        "└──────────┘"),
    5: ("┌──────────┐", 
        "│  ●    ●  │", 
        "│     ●    │", 
        "│  ●    ●  │", 
        "└──────────┘"),
    6: ("┌──────────┐", 
        "│  ●    ●  │", 
        "│  ●    ●  │", 
        "│  ●    ●  │", 
        "└──────────┘")
} # Create all 6 dice art

dice = []
total = 0
num_of_dice = int(input("How many dices?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
print(dice)

# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end = "")
    print()

for die in dice:
    total += die
print(f"total: {total}")