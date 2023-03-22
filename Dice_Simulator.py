import random
while True:
    ask = int(input("\tEnter 1 to Roll the Dice,\n\tto stop press any key other than 1--->"))
    if ask == 1:
        result = random.randint(1,6)
        print(f"\n:::The Dice says =>{result}\n")
        # ask = int(input("\n\n\tEnter 1 to Roll the Dice,\n\tto stop press any key other than 1--->"))
    else:
        break
