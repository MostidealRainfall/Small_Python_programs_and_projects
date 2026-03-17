# We're gonna need tuples for this quiz game
questions = ("What is a white-hat developer?: ",
             "What is considered the best programming language for beginners to learn?: ",
             "What programming language is considered simpler than Python?: ",
             "Is 1kg of feathers heavier or lighter than 1kg of steel?: ",
             "IS AI art superior than hand-drawn art?: ")

options = (("A. A dev wearing a white hat", 
            "B. A dev doing good things in the cyberspace", 
            "C. I dunno", 
            "D. A dev with malicious intent online"), 
           ("A. C++", 
            "B. Java", 
            "C. Javascript", 
            "D. Python"), 
           ("A. Lua", 
            "B. PhP", 
            "C. Python3", 
            "D. Rust"), 
           ("A. Heavier", 
            "B. Lighter", 
            "C. Equal in weight", 
            "D. But its a kilogram of feathers???"), 
           ("A. Yes!", 
            "B. NO!", 
            "C. Absolutely not!", 
            "D. If you like AI art, kill yourself NOW"))
answers = ("B", "D", "A", "C", "D")
guesses = []
score = 0
ques_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[ques_num]:
        print(option)
    guess = input("Enter (A B C D): ").upper()
    if guess == answers[ques_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[ques_num]} is the correct answer!")
    ques_num += 1

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")
print("answers: ", end="")

for answer in answers:
    print(answer, end=" ")
print()
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")