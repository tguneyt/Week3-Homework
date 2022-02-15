"""
Tayyip Güney 13.02.2022
Reading Number

Write a function that outputs the transcription of an input number with two digits.

Example:
28---------------->Twenty Eight
"""
num=int(input("\nNumber : "))

def read_number(x):
    """
    this program, outputs the transcription of 
    an input number with two digits.
    """
    first_n=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    sec_n=["Twenty","Thirty","Fourty","Fiffty","Sixty","Seventy","","Ninty"]
    ten_n=["Ten","Eleven","Twelwe","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen"]
    if (x//10==1):
        print("\n"+str(x),"---------------->",ten_n[x%10])
    else:
        print("\n"+str(x),"---------------->",sec_n[(x//10)-2],first_n[(x%10)-1])

read_number(num)
