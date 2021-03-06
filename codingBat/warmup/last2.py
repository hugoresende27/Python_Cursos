#Given a string, return the count of the number of times that a substring length 2 appears in the string and also
# as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
#last2('hixxhi') → 1
#last2('xaxxaxaxx') → 1
#last2('axxxaaxx') → 2
#last2('13121312') → 1

def last2(str):
    if (len(str)<2):return 0
    cont = 0
    lst2 = str[-2:]
    for i in range (0,len(str)-2):
        sub = str[i:i+2]
        if sub == lst2:
            cont +=1
    return cont
    
    

print (last2('hixxhi'))
print (last2('xaxxaxaxx') )
print (last2('axxxaaxx'))