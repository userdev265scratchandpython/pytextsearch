import os, platform, builtins, time
original_print = builtins.print
original_input = builtins.input
linesprinted = 0
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
def ss(manualclear=0, delay=5):
    splash = """This project is part of
    ;;;;;;;;;:#▒;;#▒#▒;#▒:############▒:;;;;;;;;;;;;
    ;;;;;;;;;:#▒:#▒:;##▒:#▒#▒:;;;#▒;;;;;;;;;;;;;;
    ;;;;;;;;;::#▒#▒:#▒#▒#▒#▒#▒;:;;#▒;;;;;;;;;;;;;;
    ;;;;;;;;;::#▒#▒:#▒#▒#▒#▒:###▒;;#▒the:WINST:project:;;;;;
    ;;;;;;;;;::#▒#▒:#▒#▒#▒#▒;;#▒:;#▒;;;;;;;;;;;;;;
    ;;;;;;;;;::#▒#▒:#▒#▒:##▒;;#▒:;#▒;;;;;;;;;;;;;;
    ;;;;;;;;;:;#▒##▒##▒;######▒;;#▒;;;;;;;;;;;;;;""".replace("#", "@").replace(";", "▓▓").replace(":", "▓").replace("@", " ")
    for I in splash.split("\n"):
        printme(I)
    if os.name == "nt":
        osname = "Windows"
    elif os.name == "posix":
        osname = "Linux or MacOS"
    elif os.name == "java":
        osname = "unknown(running in JVM)"
    else:
        osname = "unknown(unknown value)"
    printme(f"OS : {osname} on {platform.machine()}")
    if manualclear == 1:
        inputme("press enter to clear...")
    else:
        time.sleep(delay)
    clear(linesprinted)
if __name__ == "__main__":
    printme("This is meant to be used as a module and not as an application.")