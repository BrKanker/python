#
# #Задание №1
#
# import time
#
#
# class TrafficLight:
#     __color = 'red'
#
#     def running(self):
#         print('Светофор работает')
#
#         self.__color = 'red'
#         print(f'Установлен цвет: {self.__color}')
#         time.sleep(7)
#
#         self.__color = 'yellow'
#         print(f'Установлен цвет: {self.__color}')
#         time.sleep(2)
#
#         self.__color = 'green'
#         print(f'Установлен цвет: {self.__color}')
#         time.sleep(5)
#
#         while True:
#             self.running()
#
#
# traff_light = TrafficLight()
# print(traff_light.running())
#
# #Задание №2
#
# class Road:
#     _length = None
#     _width = None
#     __asphalt = 25 #кг
#     __depth = 0.05 #м
#
#     def __init__(self, length, width):
#         self._width = width
#         self._length = length
#
#     def calculate(self):
#         return self._length * self._width * self.__asphalt * self.__depth
#
#
# road = Road(length=4000, width=25)
# print(road.calculate())

# # #Задание №3
#
#
# class Worker:
#
#     name = None
#
#     surname = None
#
#     position = None
#
#     _income = {
#         'wage': 'wage',
#         'bonus': 'bonus'
#     }
#
#
# class Position(Worker):
#
#     def __init__(self, name:str, surname:str, wage:float, bonus:float):
#         self.name = name
#         self.surname = surname
#         self._income['wage'] = wage
#         self._income['bonus'] = bonus
#
#     def get_full_name(self):
#         return self.name + self.surname
#
#     def get_total_income(self):
#         return self._income['wage'] + self._income['bonus']
#
#
# position = Position(name="Ivan", surname="Ivanov", wage=12.33, bonus=12.33)
#
# print(position.get_full_name())
# print(position.get_total_income())
#
#Задача №4
#
# class Car:
#
#     speed: float
#     color: str
#     name: str
#     is_police: bool
#
#     def go(self):
#         return print('Поехали')
#
#     def stop(self):
#         return print('Приехали')
#
#     def turn(self, direction):
#         return print(f'Направляемся {direction}')
#
#     def show_speed(self):
#         return self.speed
#
#
# class PoliceCar(Car):
#     is_police = True
#     name = 'FORD'
#     color = 'White and black'
#     speed = 100.0
#
# class TownCar(Car):
#     is_police = False
#     name = "Jiguli"
#     color = "Rjavyi"
#     speed = 80.0
#
#     def show_speed(self):
#         if self.speed > 60:
#             return 'Превышение скорости!! ' + str(self.speed)
#         return str(self.speed)
#
# class WorkCar(Car):
#     is_police = False
#     name = 'Kamaz'
#     color = 'Orange'
#     speed = 80
#
#     def show_speed(self):
#         if self.speed > 40:
#             return 'Превышение скорости!! ' + str(self.speed)
#         return str(self.speed)
#
# class SporCar(Car):
#     is_police = False
#     name = 'ferrari'
#     color = 'Red'
#     speed = 180.0
#
#
#
# tc = TownCar()
# pc = PoliceCar()
# sc = SporCar()
# wc = WorkCar()
#
# print(tc.__dict__)
# print(pc.__dict__)
# print(wc.__dict__)
# print(sc.__dict__)
#
# pc.go()
# print(wc.turn(direction='туда'))
# sc.speed = 10000
#
# print(tc.__dict__)
# print(pc.__dict__)
# print(wc.__dict__)
# print(sc.__dict__)
#
# #Задача №5
#
# class Stationery:
#     title: str
#
#     def draw(self):
#         return 'some basic stuff'
#
# class Pen(Stationery):
#     title = 'Pen'
#
#     def draw(self):
#         return self.title
#
# class Pencil(Stationery):
#     title = 'Pencil'
#
#     def draw(self):
#         return self.title
#
# class Handle(Stationery):
#     title = 'Handle'
#
#     def draw(self):
#         return self.title
#
#
# p = Pen()
# pc = Pencil()
# h = Handle()
# s = Stationery()
#
# print(s.draw())
# print(h.draw())
# print(p.draw())
# print(pc.draw())