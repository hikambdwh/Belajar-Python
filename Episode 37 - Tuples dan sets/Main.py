# list
# menggunakan kurung siku
data_list = [10,2,4,3,2] 
print(data_list)

# tuples
data_tuples = (7,8,9,10)
print(data_tuples)
print(data_tuples[1])

# tidak bisa dilakukan
# data_tuples[1] = "ucup"
# data_tuples.append(1)

# sets (himpunan)
sets1 = {1,3,5,4,10}
sets2 = {1,4,2,5,9}

# Union
print(sets1.union(sets2))
print(len(sets1.union(sets2)))

# Difference
print(sets1.difference(sets2))
print(sets2.difference(sets1))
print(sets1.symmetric_difference(sets2))

# Intersection
print(sets1.intersection(sets2))