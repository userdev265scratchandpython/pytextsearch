found = []
file = input("File << ")
pattern = input("keyword(semicolons for or, ampersand for and, any of the two to separate) << ").split(";")
try:
    with open(file.strip("'"), "r", encoding="utf-8", errors="ignore") as f:
        for I in f.read().split("\n"):
            if not I in found:
                for Y in pattern:
                    badand = len(Y.split("&"))
                    for Z in Y.split("&"):
                        if Z.lower() in I.lower():
                            badand -= 1
                    if badand == 0:
                        found.append(I)
except FileNotFoundError:
    pass
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
