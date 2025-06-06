''' Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
вычисления площади и периметра.'''

class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color, "Circle")
        self.radius = radius
        self.pi = 3.14  # число пи

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius

    def display_info(self):
        print(f"Type: {self.shape_type}")
        print(f"Color: {self.color}")
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area():.2f}")
        print(f"Perimeter: {self.perimeter():.2f}")

# Создаем экземпляр класса Circle
circle = Circle(color="Red", radius=5)

circle.display_info()
