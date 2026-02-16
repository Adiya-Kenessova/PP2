

class Person:
    # Class variable
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

# Create objects
p1 = Person("Emil", 25)
p2 = Person("Adiya", 16)

# Access class variable
print(p1.name, "is a", p1.species)  # Emil is a Homo sapiens
print(p2.name, "is a", p2.species)  # Adiya is a Homo sapiens

# Change class variable
Person.species = "Human"

print(p1.name, "is now a", p1.species)  # Emil is now a Human
print(p2.name, "is now a", p2.species)  # Adiya is now a Human
