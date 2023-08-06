# class animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# class cat(animal):
#     def __init__(self, name, color, voice):
#         super().__init__(name, color)
#         self.voice = voice
#
#     def gate_name(self):
#         return self.name
#
#     def set_name(self, name):
#         if name != '':
#             self.name = name
#
#     def __str__(self):
#         return f'Кличка животного: {self.name} Цвет животного: {self.color} Голос животного: {self.voice}'
#
# class dog(animal):
#     def __init__(self, name, color, voice):
#         super().__init__(name, color)
#         self.voice = voice
#
#     def gate_voice(self):
#         return self.voice
#
#     def gate_name(self):
#         return self.name
#
#     def set_name(self, name):
#         if name != '':
#             self.name = name
#
#     def __str__(self):
#         return f'Кличка животного: {self.name} Цвет животного: {self.color} Голос животного: {self.voice}'
#
#
# cat1 = cat('Барсик', 'Белый', 'Мяу')
# dog1 = dog('Жучка', 'Белый', 'Гав')
# print(cat1, end='\n')
# print(dog1)

def count_p(some_objekt):
    return some_objekt.count_p()

from classes.Figura import Figura
from classes.Triagle import Triagle
from classes.Rectangle import Rectangle

triagle = Triagle(15, 20, 13)
rectangle = Rectangle(15, 20)
print(count_p(triagle))
print(count_p(rectangle))



