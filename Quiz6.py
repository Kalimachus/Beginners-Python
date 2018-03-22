def countThe(countObject):
    fin = open("python-description.txt")
    for line in fin:
        countObject[0] += 1;
        countObject[1] += len(line.split());
        for chrs in line:
            countObject[2] += 1;
    print(countObject);
    
countObject = [0, 0, 0]
countThe(countObject);
