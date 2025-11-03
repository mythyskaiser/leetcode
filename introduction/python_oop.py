class Person:

    def __init__(self, name, city, country, age = 18):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
    
    def greet(self):
        print("Hello, I am from ", self.country)
    
    def migration_to_russia(self):
        self.country = "Russia"
        return self.country

p1 = Person("Emil", 22, "France")
p3 = Person("Matthew", 43, "Ohaio")
p2 = Person("Thomas", 'Paris', 'France')

class Car:
    vehicle = ""
    def __init__(self, name, model, country):
        self.name = name
        self.model = model
        self.country = country
    
    def print_info(self):
        print(f"Name: {self.name}, Model of Car: {self.model}, Made in {self.country}")

    def get_info(self):
        print("Ohayou, kono saito wa kuruma de jyouhyou desu ne")
        self.print_info()

    def __str__(self):
        return f"{self.name}, {self.model}, {self.country}, {self.vehicle}"


car1 = Car("Mitsubishi", "Sunda", "Nihon")
car1.get_info()
car1.country = "Russia"
car1.get_info()
print(car1.vehicle)
# del p1.name
# print(p1.country)
# print(p1.age)
# print(p1.name)
Car.vehicle = "Auto"
print(car1.vehicle)
Car.year_of_production = 25
print(car1.year_of_production)

class Calculator:
    def add(self, a,b):
        return a + b
    
    def multiply(self, a,b):
        return a*b

calc = Calculator()
print(calc.add(3,5))
print(calc.multiply(3,5))

print(p1.migration_to_russia())
print(p1.country)
print(car1)

class Nihon:
    def __init__(self, name):
        self.name = name
        self.prefectures = []

    def add_prefecture(self, prefecture):
        self.prefectures.append(prefecture)
        print(f"{prefecture} prefecture was captured")
    
    def remove_prefecture(self, prefecture):
        self.prefectures.remove(prefecture)
        print(f"Tenno! We have lost this prefecture {prefecture}")
    
    def show_prefectures(self):
        print("It's your prefectures")
        for prefecture in self.prefectures:
            print(f"{prefecture} prefecture")
    
tokugawa = Nihon("Tokugawa")
tokugawa.add_prefecture("Kyushu")
tokugawa.add_prefecture("Shikoku")
tokugawa.add_prefecture("Kyoutou")
tokugawa.add_prefecture("Toukyou")
tokugawa.remove_prefecture("Kyushu")
tokugawa.show_prefectures()

# del Nihon.remove_prefecture
# tokugawa.remove_prefecture("Sheet")

# class Shogunate(Nihon):
#     def __init__(self, name):
#         Nihon.__init__(self,name)

class Shogunate(Nihon):
    def __init__(self, name, age , island):
        Nihon.__init__(self,name)
        self.__ruler = "Kiribato"
        self.__age = age
        self._island = island
    def set_age(self, age):
        if age > 1900:
            raise Exception("There is no Shogunate system")
        self.__age = age
    def get_age(self):
        return self.__age
    def __validate_ruler(self, ruler):
        if type(ruler) != str:
            return False
        return True
    def change_ruler(self, ruler):
        if self.__validate_ruler(ruler):
            self.__ruler = ruler
        else:
            raise Exception("Not type")
    def get_ruler(self):
        return f"Glory to our new Shogun: {self.__ruler}"

fukuoka = Shogunate("Fukuoka", 1600, "Shikoku")
fukuoka.add_prefecture("Shukaku")
fukuoka.add_prefecture("Hiratoka")
fukuoka.show_prefectures()
print(fukuoka.get_ruler())
fukuoka.change_ruler("miyazaki")
print(fukuoka.get_ruler())
'''
polymorphism is about same-named function that can work with multiple classes, including from parent to child,
where in child class it may changed by using but not for meaning
'''
print(fukuoka.get_age())
fukuoka.set_age(1766)
print(fukuoka.get_age())
print(fukuoka._island)
# Name mangling
# print(fukuoka._Shogunate__ruler)

class Outer:
    def __init__(self):
        self.name = "Emil"
    class Inner:
        def __init__(self,outer):
            self.outer = outer
        
        def display(self):
            print(f"Outer.class.name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

class Auto:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()
    class Engine:
        def __init__(self):
            self.status = "Off"
        def start(self):
            self.status = "Running"
            print("Engine started")
        def stop(self):
            self.status = "Off"
            print("Engine stooped")
    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand}, {self.model}")
        else:
            print("Start your car's enginge first")

car = Auto("Toyota", "Allion")
car.drive()
car.engine.start()
car.drive()