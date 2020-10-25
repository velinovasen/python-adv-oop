def age_assignment(*args, **kwargs):
    dict = {}
    for x in args:
        token = x[0]
        dict[x] = kwargs[token]
    return dict
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))