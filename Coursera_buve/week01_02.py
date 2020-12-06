import sys

digit_string = sys.argv[1]
sum = int(digit_string)


for i in range(1, sum + 1):
    for j in range(1, sum + 1):
        if(j <= sum - i ):
           print(" ", end = '')
        else:
           print("#", end = '')
    print()
print()
    
   


