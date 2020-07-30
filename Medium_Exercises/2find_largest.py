def largest(list1):
    list2 = sorted(list1)
    return list2[len(list2) - 1]

print(largest([11,20,42,97,23,10]))