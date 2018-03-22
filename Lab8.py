import os

def sortFromFile(fin):
    vals = [];
    for line in fin:
        line.strip();
        num = int(line);
        vals.append(num);
    vals.sort();
    return vals;

# precondition: do not run if the list is not sorted, nor zero
def calcStats(listVals):
    #get mean
    sum =0;
    for i in range(0,len(listVals)):
        sum+= listVals[i];
    listSize = len(listVals);
    mean = sum/listSize;
    print("Mean grade is :", mean);
    #get median
    if len(listVals) % 2 == 0:
        lVal = int(listSize/2)-1;
        lVal = listVals[lVal];
        rVal = int(listSize/2);
        rVal = listVals[rVal];
        medianI= (rVal+lVal)/2;
    else:
        medianI = int(listSize/2);
        medianI = listVals[medianI];
    print("Median grade is :", medianI);
    #get mode
    count=0;
    #find highest count
    modeVals = [];
    for i in range(0,len(listVals)):
        if listVals.count(listVals[i]) >= count:
            count = listVals.count(listVals[i]);
    #find numbers with highest count:
    print("Mode grade(s) :", end = ' ');
    for i in range(0,len(listVals)):
        if listVals.count(listVals[i]) == count:
            if listVals[i] not in modeVals:
                modeVals.append(listVals[i]);
    #print numbers with the discovered highest count
    for i in range(0,len(modeVals)):
                print(modeVals[i], end = ' ');
    print("occured", count, "time(s) each",end = ' ');
    return;


try:
    fileName ="numbers-even.txt";
    fin=open(fileName);
except:
    print("Cannot find file at:", (os.getcwd() + fileName));

vals = sortFromFile(fin);
print(vals);
calcStats(vals);
fin.close();
