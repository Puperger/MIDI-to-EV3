bool = True
storage = []
c = 0

while bool == True:
    inp = input().split()
    if inp[0] != "END":    
        storage.append(inp)
    else:
        bool = False

l = len(storage)

for i in range(l-1):
    mem = []
    if storage[i][0] == "note_on":
        mem.append(storage[i][1])
    else:
        mem.append("wait")
    len = float(storage[i+1][2]) - float(storage[i][2])
    mem.append(len)
    print(*mem)
print("END")


    
    
    
    
    
    
    