t = int(input())



for _ in range(t):
    x = int(input())
    queries = []
    i = 1
    while i < 10:
        val = str(i)
        queries.append(val)
        while len(val) < 4:
            val += str(i)
            queries.append(val)
        i += 1

    index = queries.index(str(x))

    strgs = ''
    for i in range(index + 1):
        strgs += queries[i]
    print(len(strgs))


