def madlib(name, subject):
    the_madlib = "%s's favorite subject is %s." % (name, subject)
    return the_madlib

result = madlib("matt", "math")
print(result)