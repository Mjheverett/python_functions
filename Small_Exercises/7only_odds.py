def only_odds(initial):
    list_odds = []
    for initial in initial:
        if initial % 2 != 0:
            list_odds.append(initial)
    return list_odds

result = only_odds([11,20,42,97,23,10])
print(result)