def only_evens(initial):
    list_evens = []
    for initial in initial:
        if initial % 2 == 0:
            list_evens.append(initial)
    return list_evens

result = only_evens([11,20,42,97,23,10])
print(result)