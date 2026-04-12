from random import choice

responses = [
    "Yes", "No", "Probably", "Maybe", "I don't think so",
    "Perhaps", "It's possible", "Yes, I think so"
]

print("Welcome to the Magic 8 Ball!")

while True:
    question = input("Ask me a question: ")
    print(choice(responses))

    play = input("Would you like to play again? (Y/N) ").strip().lower()
    print()

    if play == "y":
        continue
    elif play == "n":
        print("Goodbye!")
        break
    else:
        print("I didn't quite catch that.")