abc = 'abcdefghijklmnopqrstuvwxyz'
count = 0
letters= {}
for i in abc:
    letters[i] = count
    count +=1
word1 = 'assinterpretation'
word2 = 'masrepresentation'

num1 =0
num2 =0
for i in range(len(word1)):
    for key in letters.keys():
        if word1[i] == key:
            num1 = letters[word1[i]]
        if word2[i] == key:
            num2 = letters[word2[i]]

    if num1 == num2:
        continue
    elif num1 < num2:
        print(word1,'comes first')
        break
    else:
        print(word2,'comes first')
        break




