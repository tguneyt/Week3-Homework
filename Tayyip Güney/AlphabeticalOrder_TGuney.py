"""
Tayyip GÜNEY 14.02.2022
Alphabetic Order

Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words. 

Example:
Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
"""

inp=input("input the different words with (-) : ").split("-")
inp.sort()
# i=inp.split("-")
# i.sort()

def sort_words(st_word):
    # s="-".join(st_word)
    # return s
    return "-".join(st_word)

print(sort_words(inp))

