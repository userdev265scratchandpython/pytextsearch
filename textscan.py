# DO NOT EDIT LINE BELOW UNLESS MAKING UPDATE
# v::1.0.2s
# DO NOT EDIT LINE ABOVE UNLESS MAKING UPDATE
# global OR, per-group AND
# Will this code work even if it's ugly?
# by userdev265scratchandpython(https://github.com/userdev265scratchandpython)
# optionnal but recommended
import builtins
from rich import print as print
from rich.console import Console
from rich.prompt import Prompt
input = Prompt.ask
console = Console(highlight=False)
print = console.print
builtins.print = print
import splash
splash.ss(color=True)
print("[yellow]pytextsearch[/yellow]")
import hashlib, sys, http.client
script_file = sys.argv[0]
with open(script_file, "rb") as f:
    script_bytes = f.read()
    script_hash = hashlib.sha256(script_bytes).hexdigest()
print(f"[cyan]Script hash: {script_hash}[/cyan]")
with open(script_file, "r") as f:
    lines = f.read().split("\n")
    verline = lines[1] # 2nd line, 1st line has ID of 0
    ver = verline.split("v::")[1] # Version
print(f"[cyan]Version : {ver}[/cyan]")
# check legitimacy
# --get
host = "raw.githubusercontent.com"
path = "/userdev265scratchandpython/pytextsearch/refs/heads/main/versions.txt"
versinfo = ""
hashes = ["9d6b9e304282f3ae4e0f310ef0361950cca7a465e24e6166cfafb24b632628fa", "279db3f1c8e549770a1f2598431b1a8792394154adcde5b1a35ceac87c928211"]
if "0afc74a81a51b7b0d8c79ba3144ad82fedd00c69e60e2ac45afb2199ecff0a47" != hashlib.sha256(bytes(path.encode())).hexdigest():
    print("[red]This application has been modified and will not work under any circumpstances. Please delete this from your computer and report this software online. This software is PyTextSearch by Userdev265scratchandpython. If you saw this message online and can communicate with me, please do it as soon as possible.[/red]")
    exit(255)
try:
    # Connect via HTTPS
    conn = http.client.HTTPSConnection(host, timeout=10)
    conn.request("GET", path)
    response = conn.getresponse()
    if response.status == 200:
        # Read the content and save to a file
        data = response.read().decode("utf-8")
        versinfo = data.split("\n")
        print("[green]File downloaded successfully![/green]")
        conn.close()
    elif response.status == 404:
        print("[yellow]File not found[/yellow]")
    else:
        print("[red]Other error[/red]")
except Exception as e:
    print(f"[red]Error connecting to server: {e}[/red]")
# --phrase
try:
    go, sphash = splash.m095(hashes)
    if go == "stop":
        print("[red]SPLASH file check failed[/red]")
        print(f"SPLASH file hash : {sphash}")
        exit(1)
    else:
        go, sphash = splash.m095("''")
        if go != "stop":
            print("[red]SPLASH file check failed[/red]")
            print(f"SPLASH file hash : {sphash}")
            exit(1)
        go, sphash = splash.m095(script_hash)
        if go != "stop":
            print("[red]SPLASH file check failed[/red]")
            print(f"SPLASH file hash : {sphash}")
            exit(1)
    print("[green]SPLASH file check succeeded[/green]")
    go, sphash = splash.k095(hashes)
    if go == "stop":
        print("[red]dep0 file check failed[/red]")
        print(f"dep0 file hash : {sphash}")
        exit(1)
    else:
        go, sphash = splash.k095("''")
        if go != "stop":
            print("[red]dep0 file check failed[/red]")
            print(f"dep0 file hash : {sphash}")
            exit(1)
        go, sphash = splash.k095(script_hash)
        if go != "stop":
            print("[red]dep0 file check failed[/red]")
            print(f"dep0 file hash : {sphash}")
            exit(1)
    print("[green]dep0 file check succeeded[/green]")
    if versinfo != "":
        for I in versinfo:
            if I.split("::")[0] == ver:
                if I.split("::")[1] == script_hash:
                    print("[green]Legitimate[/green]")
                    break
                else:
                    print("[red]Illegitimate[/red]")
                    exit(1)
                    break
            else:
                if I == versinfo[len(versinfo)-1]:
                    print("[red]Illegitimate or Unregistered, please get the latest version from the official repository[/red]")
                    
    else:
        print("[yellow]Unable to verify![/yellow]")
except Exception as e:
    print(f"[red]Error : {e}[/red]")
    exit(1)
found = []
file = input("File ")
pattern = input("keyword(semicolons for or, ampersand for and, any of the two to separate) ").split(";")
try:
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        for I in f.read().split("\n"):
            if not I in found:
                for Y in pattern:
                    badand = len(Y.split("&"))
                    for Z in Y.split("&"):
                        if Z.lower() in I.lower():
                            badand -= 1
                    if badand == 0:
                        found.append(I)
except Exception as e:
    print(f"[red]An error occured : {e}[/red]")
print("found matches :")
if len(found) > 0:
    for I in found:
        print(f"{I}")
else:
    print("no matches found")
input("")
exit(0)
