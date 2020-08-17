# Task 1
# A Person class
# Make a class called Person. Make the __init__()
# method take firstname, lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        try:
            self.age = int(age)
        except:
            self.age = 0
            raise ValueError("Возраст должен быть числом")

    def talk(self):
        talk_person = f"Привет, меня зовут {self.firstname} {self.lastname}, мне {self.age} лет."
        return talk_person

person_1 = Person("Иван", "Иванов", 27)  # Число лет лучше хранить как число. 
print(person_1.talk())
