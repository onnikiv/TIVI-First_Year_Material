class Dog:
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Koira on nimeltään {self.name}. {type(self)}"


dog1 = Dog("Rekku")
dog2 = Dog("Musti")

print(dog1)
print(dog2)

list1 = [1, 2, 3]
print(list1)
