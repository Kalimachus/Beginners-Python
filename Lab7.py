"""
Precondition: the object must exist in the dictionary to run.
"""
def r_lookUp(d,val):
    for key in d:
        if d[key] == val:
            return key
    raise LookupError()
"""
Precondition: padding size must match or exceed the values string length
"""
def padJustifyRight(paddingWidth, outString):
    outString = str(outString);
    sLen = len(outString);
    if paddingWidth < sLen:
        return "Error"
    else:
        res = " " *(paddingWidth - sLen) + outString;
        return res;

fin = open("words.txt");
d = dict();
for line in fin:
    for c in line:
        if c >= 'a':
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
                

for vals in sorted(d.values()):
    print(r_lookUp(d, vals), ':', padJustifyRight(7,vals))
