from audiolazy import str2freq

bool = True
storage = []

while bool == True:
    inp = input().split()
    if inp[0] != "END":    
        storage.append(inp)
    else:
        bool = False

def Print():
    print("Sub Music")
    print("    StartBlock")
    for x in range(len(storage)):
        if storage[x][0] == "wait" and float(storage[x][1]) >= 0.005:
            print("    WaitFor(Wait.Timer "+ str(round(float(storage[x][1]), 2))+")")
        elif storage[x][0] != "wait":
            print("    Sound.Tone "+ str(str2freq(storage[x][0])) + ", " + str(storage[x][1]) + ", 100, WaitForCompletion")
Print()