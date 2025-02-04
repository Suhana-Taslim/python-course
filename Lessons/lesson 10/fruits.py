class fruits:
    name = "Apple"
    color = "Red"
    taste = "Sweet"
    size = 30

    def introduction(self):
        print("Hi I am a Fruit and")

    def details(self):
        print("My name is",self.name)
        print("I am in ",self.color,"Color")
        print("I taste ",self.taste)
        print("I am ",self.size,"centimeters tall")

apple = fruits()
apple.introduction()
apple.details()         