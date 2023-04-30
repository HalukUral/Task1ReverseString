
## Reverse String Task

# First option

def reverseString1(reverse):
    print("Reverse string first way:", reverse[::-1])

#Second option
def reverseString2(reverse):
    str=""
    for i in reverse:
        str=i+str
    print("Reverse string second way:",str)

result=input("Write a string:")
reverseString1(result)
reverseString2(result)