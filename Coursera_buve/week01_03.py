import sys 
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

d_d = b**2-(4*a*c)
d = d_d**(1/2)
sol1 = ((-b)+d) / (2*a)
sol2 = ((-b)-d) / (2*a)

print(int(sol1))
print(int(sol2))
