""""
Tayyip Güney 13.02.2022
Perfect Number

Perfect number is a positive integer that is equal to the sum of its proper divisors. 
The smallest perfect number is 6, which is the sum of 1, 2, and 3. Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128. 
Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

"""
from functools import reduce

def find_perfect(num):    
    """
    This function is written to for find a positive integer 
    that is equal to the sum of its proper divisors
    """
    div=0                 
    for i in range(1,num): 
        if num%i == 0:      # Is the parameter of the function proper divisible?           
            div=div+i       # sum proper divisors
    if div==num:            # if the sum of proper divisors is equal to the parameter    
        return div
                 
num_until=1000      #up to which number

print(f"\nsum of perfect numbers until {num_until} is "+
      f"{reduce(lambda x,y: x+y,list(filter(find_perfect,range(1,num_until+1))))}\n")

# print(list(filter(find_perfect,range(1,num_until+1))))       # list of perfect numbers
# reduce(lambda x,y: x+y,list_perfect_numbers))                # sum of perfect numbers



