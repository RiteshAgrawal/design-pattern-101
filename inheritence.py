from abc import ABC, abstractmethod


class Animal(ABC):
    TYPE = 'Animal'

    def get_type(self):
        return self.TYPE

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    TYPE = 'Dog'

    def speak(self):
        return "Bark"


class Cat(Animal):
    TYPE = 'Cat'

    def speak(self):
        return "Meow"


if __name__ == '__main__':
    d = Dog()
    print(d.speak(), d.get_type())
    c = Cat()
    print(c.speak(), c.get_type())
