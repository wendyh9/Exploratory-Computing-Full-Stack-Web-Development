import string

word = input("Enter a word: ")
count = 0

# all lowercase 
# remove punctuation
# if '-', needs to replace with a space

with open('PythonSummary.txt', 'r') as f:
   text = f.read()
   text_arr = text.split()
   for x in text_arr:
        x = x.lower()
        if ('-' in x):
            index = x.index('-')
            temp = x[index + 1:len(x)]
            x = x[0:index]
            text_arr.append(temp)
        x = x.translate(str.maketrans('','',string.punctuation))
        if x == word:
            count += 1

print(f'The word {word} occurs {count} times')
