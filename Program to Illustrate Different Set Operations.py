E = {0, 1, 2, 3, 4, 5, 6, 8}
N = {2, 4}
#union
union_r = E.union(N)
print("Union of E and N:", union_r)
# Intersection 
intersection_result = E.intersection(N)
print("Intersection of E and N:", intersection_result)

# Difference 
difference_result = E.difference(N)
print("Difference of E and N:", difference_result)

# Symmetric 
symmetric_difference_result = E.symmetric_difference(N)
print("Symmetric difference of E and N:", symmetric_difference_result)
