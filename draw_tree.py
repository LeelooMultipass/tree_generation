def Tree(n, l, b):
    leaves = n/2
    base = n/2-1
    for i in range(1, n+1):
        if(i%2 != 0):
            print "    " * leaves, l* i
            leaves -=1
    print "    " * base, b * 3

Tree(21, '@', '#')

