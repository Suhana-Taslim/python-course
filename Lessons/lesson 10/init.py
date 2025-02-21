class Parrot:

    species = "Bird"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

Jack = Parrot("Jack", 5, "Green")
Jicky = Parrot("Jicky", 4, "White")

print("Jack is a {}".format(Jack.species))
print("Jicky is a {}".format(Jicky.species))

print("{} is {} years old and {} in color".format(Jack.name, Jack.age, Jack.color))
print("{} is {} years old and {} in color".format(Jicky.name, Jicky.age, Jicky.color))
