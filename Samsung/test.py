people = [[(1, 3), 5], [(3, 7), 3], [(3, 5), 3]]
people.sort(key=lambda x:(x[1], x[0]))
print(people)
print((1,3) in people[2])
