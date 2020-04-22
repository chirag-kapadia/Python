def lists(x):
    print("Original : ", x)
    print("Address :", id(x))

    x[2] = 400
    print("Updated : ", x)
    print("Address Updated :", id(x))


lst = [100, 200, 300]
lists(lst)
print(lst)
