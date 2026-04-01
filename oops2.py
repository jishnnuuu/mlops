class Animal:
    def __init__(self):
        self.name = "Benny"
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak() #calls the speak method of the parent class
        print(f"{self.name} barks and it is {self.breed}")

dog1 = Dog("golden retriever")
dog1.speak()
