#co-program

def grep(pattern):

    print("start grep")
    try:
       while True:
           line = yield
           if pattern in line:
            print(line)
    except GeneratorExit:
        print("stop grep")
        
#####
g = grep("py")
next(g)

###ex_01
# g.send("go is better?")
# g.send("py is simple!")
# g.close()

###ex_02
g.throw(RuntimeError, "something_wrong")