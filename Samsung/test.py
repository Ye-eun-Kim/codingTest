import copy
blocks = [1,2,3,4,5]
block = blocks[3]
print(block)
block = 7
print(block)
b = copy.deepcopy(blocks)
b[0] = 4
print(b)