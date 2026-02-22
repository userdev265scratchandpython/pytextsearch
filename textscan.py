# DO NOT EDIT LINE BELOW UNLESS MAKING UPDATE
# v::1.0.0
# DO NOT EDIT LINE ABOVE UNLESS MAKING UPDATE
# global OR, per-group AND
# Will this code work even if it's ugly?
# by userdev265scratchandpython(https://github.com/userdev265scratchandpython)
print("pytextsearch")
import hashlib, sys, http.client
script_file = sys.argv[0]
with open(script_file, "rb") as f:
    script_bytes = f.read()
    script_hash = hashlib.sha256(script_bytes).hexdigest()
print(f"Script hash: {script_hash}")
with open(script_file, "r") as f:
    lines = f.read().split("\n")
    verline = lines[1] # 2nd line, 1st line has ID of 0
    ver = verline.split("v::")[1] # Version
print(f"Version : {ver}")
# check legitimacy
# --get
host = "raw.githubusercontent.com"
path = "/userdev265scratchandpython/pytextsearch/refs/heads/main/versions.txt"
versinfo = ""
try:
    # Connect via HTTPS
    conn = http.client.HTTPSConnection(host, timeout=10)
    conn.request("GET", path)
    response = conn.getresponse()
    if response.status == 200:
        # Read the content and save to a file
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
# --phrase
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
