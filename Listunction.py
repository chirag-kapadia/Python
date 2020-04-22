def funList(x):
    even = 0
    odd = 0
    print("List : ", x)
    for i in x:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd


lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
even1, odd1 = funList(lst)
print("Even number is : ", even1)
print("Odd Number is : ", odd1)
