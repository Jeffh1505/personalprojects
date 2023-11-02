class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(s):
        return f"*woof* {s} *woof*"
    
    def __repr__(self):
        return "The dog's name is {}".format(self.name)
    

print(Dog("Clifford"))
print(Dog.speak("Hello"))