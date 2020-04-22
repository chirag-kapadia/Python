import array as arr

marks = arr.array('i', [])  # Empty Array Created

value1 = int(input("Enter a size of Array : "))
for i in range(value1):
    value2 = int(input("Enter a Elements : "))
    marks.append(value2)
print(marks)
