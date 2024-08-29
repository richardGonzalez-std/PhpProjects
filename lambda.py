people = [
    {
        "name": "Harry","house":"Gryffindor"
    },
    {
        "name": "Cho", "house":"Ravenclaw"
    },
    {
        "name":"draco", "house": "Slytherin"
    }
]

def f(person):
    return person["name"]

people.sort(key=lambda person: person["name"],reverse=True)
print(people)