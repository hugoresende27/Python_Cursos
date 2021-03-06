# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    soma=0
    if (len(nums)>0): 
        i=0
        while i<len(nums):
            if (nums[i]!=13):
                soma += nums[i]
                i+=1
            else :
                i+=2
                continue
        return soma
    else : return 0
    
    
print(sum13([1, 2, 2, 1]) )
print(sum13([1, 1]) )
print(sum13([1, 2, 2, 1, 13]))
print (sum13([13, 1, 2, 13, 2, 1, 13]) ) #3
print (sum13([5, 13, 2]))