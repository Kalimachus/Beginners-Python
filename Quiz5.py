def both_ends_are_consonants(word):
    result = word.lower();
    rVal = len(result)-1;
    if(result[0] != 'a' and result[rVal] !='a'):
        if(result[0] != 'e' and result[rVal] !='e'):
            if(result[0] != 'i' and result[rVal] !='i'):
                if(result[0] != 'o' and result[rVal] !='o'):
                    if(result[0] != 'u' and result[rVal] !='u'):
                        return True;
    return False;

print(both_ends_are_consonants("Bookkeeping"))
print(both_ends_are_consonants("Octuplet"))