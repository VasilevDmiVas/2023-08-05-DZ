from classes.Metod import Metod


class Stroka(Metod):
    def __init__(self, text, text1, text2, text3):
        self.text = text
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3

    def dlinaStroka(self):
        return len(self.text)

    def get_dlinaStroka(self):
        return self.dlina()

    def inStroka(self):
        return (self.text1 in self.text)

    def get_inStroka(self):
        return self.inStroka()

    def zamenaStroka(self):
        text4 = ''
        for index in self.text:
            if index != self.text2:
                text4 += index
            else:
                text4 += self.text3
        self.text = text4
        return self.text

    def get_zamenaStroka(self):
        return self.zamenaStroka()

    def __str__(self):
        return f' Количество символов в строке: {self.text} =  {self.dlinaStroka()}\n ' \
        f'Cтрокa содержит символ? "{self.text1}" Ответ: {self.inStroka()}\n' \
        f' В строке заменяем символ "{self.text2}" на символ: {self.text3} получаем {self.zamenaStroka()}'
