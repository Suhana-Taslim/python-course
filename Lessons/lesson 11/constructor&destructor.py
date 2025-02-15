class Animals:
    name = "cat"

    def __init__(self):
        print("The name is",self.name)
        print('Animals Created.')

    def __del__(self):
        print('Destructor called, Animals deleted.')   

obj = Animals()
del obj         