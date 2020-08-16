# Task 2
# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which return the dog’s age in human equivalent.

class Dog():
    age_factor = 7

    def __init__(self, age_dog):
        self.age_dog = age_dog

    def human_age(self):
        age_dog_as_human = int(self.age_dog) * self.age_factor
        return age_dog_as_human


age = input('Введите возраст Вашей собаки:')
is_dog = Dog(int(age))
print(f'Если бы Ваша собака была человеком, ей бы было {is_dog.human_age()}')