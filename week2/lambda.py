people = [{"name": "Harry", "house": "Gryffinder"},
{"name": "Cho","house": "Ravenclaw"},
{"name": "Draco","house": "Slytherin"}
] 

#def f(person):
#    return person["house"]

people.sort(key=lambda person:person["name"])

print(people)
