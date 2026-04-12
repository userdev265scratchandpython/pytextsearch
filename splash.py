import os, platform, builtins, time, hashlib
original_print = builtins.print
original_input = builtins.input
def ss(manualclear=0, delay=5, color=False):
    from mwinst import printme, inputme, clear
    if os.name == "nt":
        home = f"C:/Users/{os.getlogin()}/"
    elif os.name == "posix":
        if os.path.exists("/home"):
            home = f"/home/{os.getlogin()}/"
        else:
            home = f"/Users/{os.getlogin()}/"
    if not os.path.exists(f"{home}.winstsplash-ignore"):
        if not color:
            splash = """This project is part of
;;;;;;;;;:#▒;;#▒#▒;#▒:############▒:;;;;;;;;;;;;
;;;;;;;;;:#▒:#▒:;##▒:#▒#▒:;;;#▒;;;;;;;;;;;;;;
;;;;;;;;;::#▒#▒:#▒#▒#▒#▒#▒;:;;#▒;;;;;;;;;;;;;;
;;;;;;;;;::#▒#▒:#▒#▒#▒#▒:###▒;;#▒the:WINST:project:;;;;;
;;;;;;;;;::#▒#▒:#▒#▒#▒#▒;;#▒:;#▒;;;;;;;;;;;;;;
;;;;;;;;;::#▒#▒:#▒#▒:##▒;;#▒:;#▒;;;;;;;;;;;;;;
;;;;;;;;;:;#▒##▒##▒;######▒;;#▒;;;;;;;;;;;;;;
Welcome to the WINST project's first tool, pytextsearch""".replace("#", "@").replace(";", "▓▓").replace(":", "▓").replace("@", " ")
        else:
            splash = """This project is part of
[red];;;;;;;;;:#▒;;#▒#▒;#▒:############▒:;;;;;;;;;;;;[/red]
[green];;;;;;;;;:#▒:#▒:;##▒:#▒#▒:;;;#▒;;;;;;;;;;;;;;[/green]
[blue];;;;;;;;;::#▒#▒:#▒#▒#▒#▒#▒;:;;#▒;;;;;;;;;;;;;;[/blue]
[cyan];;;;;;;;;::#▒#▒:#▒#▒#▒#▒:###▒;;#▒the:WINST:project:;;;;;[/cyan]
[yellow];;;;;;;;;::#▒#▒:#▒#▒#▒#▒;;#▒:;#▒;;;;;;;;;;;;;;[/yellow]
[purple];;;;;;;;;::#▒#▒:#▒#▒:##▒;;#▒:;#▒;;;;;;;;;;;;;;[/purple]
[brown];;;;;;;;;:;#▒##▒##▒;######▒;;#▒;;;;;;;;;;;;;;[/brown]
Welcome to the WINST project's first tool, pytextsearch""".replace("#", "@").replace(";", "▓▓").replace(":", "▓").replace("@", " ")
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
        if not color:
            clear(linesprinted)
        with open(f"{home}.winstsplash-ignore", "w") as f:
            f.write("")
    print(f"{'[cyan]'*color}This project is part of the Winst project{'[/cyan]'*color}")
def m095(hashes):
    script_file = "splash.py"
    with open(script_file, "rb") as f:
        script_bytes = f.read()
        script_hash = hashlib.sha256(script_bytes).hexdigest()
    if not script_hash in hashes:
        return "stop", script_hash
    elif not len(hashes) == secfeatures:
        return "stop", script_hash
    else:
        return "continue", script_hash
def k095(hashes):
    script_file = "mwinst.py"
    with open(script_file, "rb") as f:
        script_bytes = f.read()
        script_hash = hashlib.sha256(script_bytes).hexdigest()
    if not script_hash in hashes:
        return "stop", script_hash
    elif not len(hashes) == secfeatures:
        return "stop", script_hash
    else:
        return "continue", script_hash
secfeatures = 2
if __name__ == "__main__":
    printme("This is meant to be used as a module and not as an application.")