    N = int(input())
    tl = []
    for i in range (N):
        a = input().split()

        if a[0] == "insert":
            tl.insert(int(a[1]),int(a[2]))
        elif a[0] == "print":
            print(tl)
        elif a[0] == "remove":
            tl.remove(int(a[1]))
        elif a[0] == "append":
            tl.append(int(a[1]))
        elif a[0] == "sort":
            tl.sort()
        elif a[0] == "pop":
            tl.pop()
        else:
             tl.reverse()
        
