class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class cat(animal):
    def __int__(self, name, color, voice):
        super().__int__(name, color)
        self.voice = voice

    def gate_name(self):
        return self.name

    def set_name(self, name):
        if name != '':
            self.name = name

    def __str__(self):
        return f'Кличка животного: {self.name} Цвет животного: {self.color} Голос животного: Мяу'

class dog(animal):
    def __int__(self, name, color, voice):
        super().__int__(name, color)
        self.voice = voice

    def gate_voice(self):
        return self.voice

    def gate_name(self):
        return self.name

    def set_name(self, name):
        if name != '':
            self.name = name

    def __str__(self):
        return f'Кличка животного: {self.name} Цвет животного: {self.color} Голос животного: Гав'


cat1 = cat('Барсик', 'Белый')
dog1 = dog('Жучка', 'Белый')
print(cat1, end='\n')
print(dog1)