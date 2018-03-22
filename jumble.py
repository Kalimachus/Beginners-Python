def matchAndFindWord(strIn):
    fin = open("words.txt");
    strIn = strIn.lower();
    compStr = abecedarate(strIn);
    
    for line in fin:
        line = line.lower();
        line = line.strip();
        ref = abecedarate(line)
        if(compStr == abecedarate(line)):
            print(line,end=" ");
    return;

def abecedarate(strArg):
    a="";b="";c="";d="";e="";f="";
    g="";h="";i="";j="";k="";l="";
    m="";n="";o="";p="";q="";r="";
    s="";t="";u="";v="";w="";x="";
    y="";z="";
    for char in strArg:
        if(char == "a"):
                a+="a";
        elif(char == "b"):
                b+="b";
        elif(char == "c"):
                c+="c";
        elif(char == "d"):
                d+="d";
        elif(char == "e"):
                e+="e";
        elif(char == "f"):
                f+="f";
        elif(char == "g"):
                g+="g";
        elif(char == "h"):
                h+="h";
        elif(char == "i"):
                i+="i";
        elif(char == "j"):
                j+="j";
        elif(char == "k"):
                k+="k";
        elif(char == "l"):
                l+="l";
        elif(char == "m"):
                m+="m";
        elif(char == "n"):
                n+="n";
        elif(char == "o"):
                o+="o";
        elif(char == "p"):
                p+="p";
        elif(char == "q"):
                q+="q";
        elif(char == "r"):
                r+="r";
        elif(char == "s"):
                s+="s";
        elif(char == "t"):
                t+="t";
        elif(char == "u"):
                u+="u";
        elif(char == "v"):
                v+="v";
        elif(char == "w"):
                w+="w";
        elif(char == "x"):
                x+="x";
        elif(char == "y"):
                y+="y";
        elif(char == "z"):
                z+="z";
        else:
            print("error");
    result =a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z;
    result.strip();

    return result;

strIn = input("Enter a jumbled word of any length: ");
matchAndFindWord(strIn);
