sentence = input("Please enter a sentence: ")
times = input("Please enter how many times the sentence should be repeated: ")

with open('CompletedPunishment.txt', 'w') as file:
    for x in range(int(times)):
        file.write(sentence)
        file.write('\n')
