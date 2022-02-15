"""
Tayyip Güney 14.02.2022
"""
# https://www.hackerrank.com/challenges/capitalize/problem


def solve(s):
    name=s.lower()   
    a=""
    x=0
    for i in name:
        if x==0:
            i=i.upper()
            x=1
        if i==" ":
            x=0
        a+=i
    return a   

# name=input("Name Surname : ")

name="kEMaL 12yIlmAz"

print(solve(name))