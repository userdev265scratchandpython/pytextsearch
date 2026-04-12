import builtins
linesprinted = 0
original_print = builtins.print
original_input = builtins.input
def printme(*args, **kwargs):
    global linesprinted
    linesprinted += 1
    original_print(*args, **kwargs)
def inputme(*args, **kwargs):
    global linesprinted
    linesprinted += 1
    return original_input(*args, **kwargs)
def clear(lines):
    I = lines
    while not I == 0:
        print("\033[F\033[2K", end="")
        I -= 1