import array as arr

vals = arr.array('i', [2, 3, 5, 6, 7, 8])

# print(vals.buffer_info())
# print(vals.itemsize)

for i in range(5):
    print(vals[i])

for a in range(len(vals)):
    print(vals[a])