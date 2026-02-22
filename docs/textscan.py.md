# pytextsearch main file

:warning: All comments are skipped in documentation to shrink file size.

line 9-18
```
script_file = sys.argv[0]
with open(script_file, "rb") as f:
    script_bytes = f.read()
    script_hash = hashlib.sha256(script_bytes).hexdigest()
print(f"Script hash: {script_hash}")
with open(script_file, "r") as f:
    lines = f.read().split("\n")
    verline = lines[1]
    ver = verline.split("v::")[1]
print(f"Version : {ver}")
```
## hash and version, used just after to check legitimacy
- Hashes the file to give sha256 using hashlib and gives version from 2nd line
- that's all

line 21-40
```
host = "raw.githubusercontent.com"
path = "/userdev265scratchandpython/pytextsearch/refs/heads/main/versions.txt"
versinfo = ""
try:
    conn = http.client.HTTPSConnection(host, timeout=10)
    conn.request("GET", path)
    response = conn.getresponse()
    if response.status == 200:
        data = response.read().decode("utf-8")
        versinfo = data.split("\n")
        print("File downloaded successfully!")
        conn.close()
    elif response.status == 404:
        print("File not found")
    else:
        print("Other error")
except Exception as e:
    print(f"Error connecting to server: {e}")
```
downloads versions.txt to ram to verify legitimacy
- Requires internet
- that's all

line 42-56
```
try:
    if versinfo != "":
        for I in versinfo:
            if I.split("::")[0] == ver:
                if I.split("::")[1] == script_hash:
                    print("Legitimate")
                else:
                    print("Illegitimate")
            else:
                if I == versinfo[len(versinfo)-1]:
                    print("Illegitimate/Unregistered, please get the latest version from the official repository")
    else:
        print("Unable to verify!")
except Exception as e:
    print(f"Error : {e}-")
```
phrases downloaded file and reports legitimacy to user
- Requires all previous parts of the script
- that's all

line 47-63
```
found = []
file = input("File < ")
pattern = input("keyword(semicolons for or, ampersand for and, any of the two to separate) < ").split(";")
with open(file, "r", encoding="utf-8", errors="ignore") as f:
    for I in f.read().split("\n"):
        for Y in pattern:
            if not I in found:
                if Y.lower() in I.lower():
                    found.append(I)
print("found matches :")
if len(found) > 0:
    for I in found:
        print(f"{I}")
else:
    print("no matches found")
input("")
```
actual functionnal code
- Requires input file
- Requires pattern
- Only supports OR