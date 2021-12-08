#Given a string, return a new string where the first and last chars have been exchanged.
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
    if(len(str)>1): return str[-1:]+str[1:-1]+str[:1]
    else: return str

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))