#example: >python3 solution.py 12345

import sys

digit_string = sys.argv[1]
sum = 0

for letter in digit_string:
    b=int(letter)
    sum=sum+b
print(sum)



