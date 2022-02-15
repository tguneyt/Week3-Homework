"""
Tayyip Güney 14.02.2022
"""

# https://www.hackerrank.com/challenges/find-digits/problem

# Complete the 'findDigits' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

def findDigits(n):
    list=[]
    a=0
    for i in str(n):
        list.append(i)
    for i in range(len(list)):
        if int(list[i])!=0:
            if n % int(list[i])==0:
                a+=1                         
    # Write your code here
    return a

x=2124 # 
print(findDigits(x))