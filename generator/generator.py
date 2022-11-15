import random
from data.data import Person
from faker import Faker

faker_en = Faker('En')


def generated_person():
    return Person(email=faker_en.email())


def generated_file():
    path = rf'C:\Users\90531\360RENT_autotest_project\generator\test{random.randint(10,100)}.txt'
    file = open(path,'w')
    file.write(f"New_skill{random.randint(10,100)}")
    file.close()
    return path
