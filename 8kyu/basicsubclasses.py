class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init(name)
        self.gender = "Male"

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)
        self.gender = "Female"

class God:
    def __init__(self):
        #creating instances of Man and Woman (Adam and Eve)
        self.adam = Man("Adam")
        self.eve = Woman("Eve")

    def __getitem__(self, index):
        #Return the corresponding objects based on the index of gender
        if index == 0:
            return self.adam
        elif index == 1:
            return self.eve
        else:
            raise IndexError("Index out of range")
    def __len__(self):
        return 2


#Best solution was
#def God:
#return [Man(), Woman()]

#class Human(object):
#pass

#class Man(Human):
#pass

#class Woman(Human):
#pass
