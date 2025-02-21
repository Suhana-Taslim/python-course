class Robot:

    specie = "Robot"

    def __init__(self, name, age, color):
        self.name =name
        self.age = age
        self.color = color

Sophia = Robot("Sophia", 2, "Brown")
Sifra = Robot("Sifra", 1, "White")

print("Sophia is a {}".format(Sophia.specie))
print("Sifra is a {}".format(Sifra.specie))

print("I am {} , {} months old and {} in color".format(Sophia.name, Sophia.age, Sophia.color))
print("I am{} , {} year old and {} in color".format(Sifra.name, Sifra.age, Sifra.color))
