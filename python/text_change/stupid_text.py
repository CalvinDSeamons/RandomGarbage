import random

def scramble():
    scramble=input("Enter the phrase please.")
    sentence=[]

    for character in scramble:
        chance = random.randint(1,100)
        if chance <= 50:
            sentence.append(character.upper())
        elif chance >= 51:
            sentence.append(character.lower())

        # Special Cherry
        chance = random.randint(1,100)
        if character == 'E' or character == 'e':
            if chance <= 30:
                sentence = sentence[:-1]+['3']

        if character == 'A':
            if chance >= 75:
                sentence = sentence[:-1]+['4']

        if character == 'O' or character == 'o':
            if chance > 50:
                sentence = sentence[:-1]+['0'] 
    print(*sentence, sep="")

scramble()
