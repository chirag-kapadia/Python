def fab(f):
    # print(f)

    a = 0
    b = 1
    for i in range(f):
        c = a + b
        a = b
        b = c
        # j = i
        print(c)


fab(6)
