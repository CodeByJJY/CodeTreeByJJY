s = set()

def hashset(text):
    cmd, val = text.split()
    val = int(val)

    if cmd == "add":
        s.add(val)
    
    if cmd == "remove":
        s.remove(val)
    
    if cmd == "find":
        if val in s:    print("true")
        else:           print("false")

n = int(input())

for _ in range(n):
    command = input()
    hashset(command)