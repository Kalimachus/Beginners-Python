refChars = []
word = input("Enter a word : ")
word = word.strip()
count = 0
for i in range(len(word)):
    line = "".join(refChars)
    if word[i] in line:
        count -= 1
    elif word[i] not in line:
        refChars.append(word[i])
        count += 1
print(word, "contains", count, "unique letters")
