"""
Tayyip GÜNEY 14.02.2022
Unique List

Write a function that filters all the unique(unrepeated) elements of a given list.

Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output : [1, 2, 3, 4, 5]
"""

def unique_list(list_fun):             # first approach
    return sorted(list(set(list_fun)))


# def unique_list(list_fun):           # second approach
#     z_list=[]
#     for i in list_fun:
#         if i not in z_list:
#           z_list.append(i)  
#     return sorted(z_list)             
              
     
print("Unique List : ", unique_list([5,5,4,4,12,13,13,14,1,2,2,2,2,1,1,1,2,3,3,3,4,15,12,14]))
