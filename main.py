import numpy as np
# Student exam marks dataset (rows = students, columns = subjects)
data = np.array([
 [78, 85, 90, 88],
 [67, 72, 70, 60],
 [90, 92, 94, 96],
 [56, 65, 60, 58],
 [88, 84, 82, 86],
 [73, 75, 78, 72],
 [91, 89, 93, 90],
 [64, 68, 70, 66]
])
# copy
# data_copy=data.copy()
# data[1,2]=100
# print(data)
# print("copy:",data_copy)
# view
# data_view=data.view()
# data[1,2]=100
# print(data)
# print("view:",data_view)
# change marks
# data[0,0]=100
# print(data)
# Shape
# print(data.shape)
# print("students:",data.shape[0])
# print("subject:",data.shape[1])
# print("dimension:",data.ndim)
# Reshape
# a = data.reshape(-1)
# print(a)

# b = data.reshape(2,16)
# print(b)

# c = data.reshape(4,8)
# print(c)
# Iterating
# for x in data:
#   print(x)

# for x in data:
#   for y in x:
#     print(y)

# for x in np.nditer(data):
#   print(x)
# Join
# extra_students = np.array([
# [80, 82, 84, 86],
# [60, 62, 64, 66]
#  ])
# a = np.concatenate((data,extra_students),axis=0)
# print(a)

# b = np.vstack((data,extra_students))
# print(b)

# c = np.hstack((data,data))
# print(c)
# split
# newarr = np.array_split(a,2)
# print("2 Parts:",newarr)

# newarr = np.array_split(a,4)
# print("4 parts:",newarr)

# newarr = np.hsplit(a,4)
# print("Hsplit:",newarr)
# search
# x = np.where(data==90)
# print(x)

# x = np.where(data >90)
# print(x)

# x = np.where(data[:,0] > 85)
# print(x)

# sort
# print(np.sort(data))
# print(np.sort(data,axis =1))
# print(np.sort(data,axis =0))

filter_arr = []
for row in data:
    for marks in row:
        if marks > 80:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

# filter_arr = data > 80
# print(type(filter_arr))
filter_arr = np.array(filter_arr)
new_arr = np.array_split(filter_arr,8)
new_arr = np.array(new_arr)
fin = data[new_arr]
print(type(new_arr))
print(fin)

# for row in data:
#     print(row[0] > 85)

filter_arr = []
for i in range(32):
    filter_arr.append(False)
print(filter_arr)
counter = 0
for row in data:
    filter_arr[counter * 4] = bool(row[0] > 85)
    counter += 1
new_arr = np.array_split(filter_arr,8)
new_arr = np.array(new_arr)
fin = data[new_arr]
print(fin)


# Bonus
# print(data[np.all(data>85,axis=1)])
# print(np.max(data,axis=0))
# print(np.mean(data,axis=1))
# 0 0 
# 4 1
# 8 2
# 12 3
# 16 4
