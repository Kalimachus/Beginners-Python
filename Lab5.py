
fin=open('words.txt');
longWord, shortWord, line, word = "","","","";
shortLen,longLen, currLen,totalWords, avTotal= 0,0,0,0,0;

#do this once just for getting the first length for
# purposes of comparing the shortest word

line = fin.readline();
word = line.strip();
shortLen = len(word);
shortWord=word;
longLen = len(word);
totalWords += 1;
avTotal += len(word);

#loop for the rest of the file
for line in fin:
    word = line.strip();
    currLen = len(word);
    if(currLen > longLen):
        longLen = currLen;
        longWord = word;
    if(currLen < shortLen):
        shortLen = currLen;
        shortWord = word;
    avTotal += currLen;
    totalWords+=1;

print("The longest words are", longLen, "characters; an example is", longWord);
print("The shortest words are", shortLen, "characters; an example is", shortWord);
print("The average word length is", avTotal/totalWords);
