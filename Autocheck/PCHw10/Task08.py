class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):

    def info(self):
        s = f"{self.nickname}-{self.weight}"
        return s


class DogCat(Dog, Cat):


    def info(self):
        s = f"{self.nickname}-{self.weight}"
        return s


cat_dog = CatDog(nickname="Stas", weight=25)
print(cat_dog.say())