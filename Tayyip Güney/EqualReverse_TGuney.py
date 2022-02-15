"""
Tayyip GÜNEY 14.02.2022
Equal Reverse 

Write a function that controls the given inputs whether 
they are equal to their reversed order or not.
Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False
"""
word=input("Word : ")

def check_reverse(w):               # first approach
    """
    this function,controls the given inputs     
    whether they are equal to their reversed order or not.
    """

    return print(w==w[::-1])        

# def check_reverse(w):             # second approach
#     """
#     this function,controls the given inputs 
#     whether they are equal to their reversed order or not.
#     """
#     list=[i for i in w]
#     list2=list.copy()
#     list2.reverse()  
#     print(list==list2) 

check_reverse(word)        