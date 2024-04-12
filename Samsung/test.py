v = [[0 for i in range(5)] for j in range(5)]
v[2][2] = (5,1)
v[2][3] = (8,0)

# print(v[0].index(max(v[0][1:6])))
print(v[2].index(max(v[2][2:4])))