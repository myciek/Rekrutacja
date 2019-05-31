with open("skyphrases.txt", "r") as file:
    line = file.readline()
    correct_phrases = 0
    while line:
        phrase = line.split()
        if len(phrase) == len(set(phrase)):
            correct_phrases += 1

        line = file.readline()

file = open("answers.txt", "w+")
file.write("{} skyphrases are valid.\n".format(correct_phrases))
