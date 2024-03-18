def add_ages(**ages):
    sum = 0
    for K, v in ages.items():
        sum = sum+v
    return sum
total_age=add_ages(John=23,Tom=45,Jerry=18)
print("The total age is:",total_age)