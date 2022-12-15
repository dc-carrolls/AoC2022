
class Animal:
    def __init__(self,age,legs):
        self.legs = legs
        self.age =age
        self.x = 0

    def move(self,time):
        pass

    def __repr__(self) -> str:
        return (f"I'm an Animal:\n"
                f"with {self.legs} legs\n"
                f"{self.age} years old\n"
                f"with position x:{self.x}")
    

class Dog(Animal):
    def __init__(self, age):
        super().__init__(age, 4)
        self.speed = 10

    def move(self,time):
        self.x = self.x + self.speed * time

    def __repr__(self) -> str:
        return (f"I'm a Dog:\n"
                f"with {self.legs} legs\n"
                f"{self.age} years old\n"
                f"with position x:{self.x}")

class Human(Animal):
    def __init__(self, age):
        super().__init__(age, 2)
        self.speed = 5
        self.y=0

    def move(self,time):
        self.y = self.y + self.speed * time

    def __repr__(self) -> str:
        return (f"I'm a Human:\n"
                f"with {self.legs} legs\n"
                f"{self.age} years old\n"
                f"with position x:{self.x}\n"
                f"and position y:{self.y}")


animals_list = []

for n in range(5):
    animals_list.append(Animal(n,n+1))

for n in range(1,6):
    animals_list.append(Dog(n))

for n in range(18,23):
    animals_list.append(Human(n))

animals_list.sort(key= lambda x: x.legs, reverse=True)

for a in animals_list:
    a.move(3)
    print(a)