class Person:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def introduce(self):
        return f"Hello {self.name}, welcome to Mohican Airwars flight xyz.It says here on my record that you are {self.age} years old and {self.gender}. If that the case proceed to your seat in the column B3 and wait for further instructions"
        
person1=Person("Gallagher",26,"male")

print(person1.introduce())
    