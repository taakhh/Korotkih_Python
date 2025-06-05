'''Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.'''

import pickle

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}")

def save_def(cars, filename):
    with open(filename, 'wb') as file:
        pickle.dump(cars, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Focus", 2018)

cars_list = [car1, car2, car3]
save_def(cars_list, "cars_data.pkl")

loaded_cars = load_def("cars_data.pkl")
for car in loaded_cars:
    car.display_info()
