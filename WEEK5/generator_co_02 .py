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
        

def grep_py_coroutine():
    g =grep("py")
    yield from g

#####
g = grep_py_coroutine()
g.send(None)
g.send("py wow")

