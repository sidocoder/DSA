t = int(input().strip())
for i in range(t):    
    sentence = input().strip()
    if sentence.endswith("po"):
        print("FILIPINO")
    elif sentence.endswith("desu") or sentence.endswith("masu"):
        print("JAPANESE")
    elif sentence.endswith("mnida"):
        print("KOREAN")
