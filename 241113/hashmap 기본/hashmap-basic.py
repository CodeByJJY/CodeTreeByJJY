N = int(input())
hashmap = {}

for _ in range(N):
    command = input().split()
    cmd = command[0]
    key = int(command[1])

    if cmd == "add":
        value = int(command[2])
        hashmap[key] = value
    elif cmd == "remove":
        if key in hashmap:
            del hashmap[key]
    elif cmd == "find":
        print(hashmap.get(key, "None"))
