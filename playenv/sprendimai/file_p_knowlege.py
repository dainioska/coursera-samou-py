#file handler darymas:
f = open('sprendimai/demukas.txt', 'w')

try:
    for i in range(10):
       f.write("this is: %d\n" % (i+1))
finally:
    f.close()

##### arba su file manager:
with open('sprendimai/demoo.txt,','a') as f: 
    for i in range(10):
        f.write("this is: %d\n" % (i+11))