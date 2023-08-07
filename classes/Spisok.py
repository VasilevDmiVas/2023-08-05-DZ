from classes.Metod import Metod


class Spisok(Metod):
    def __init__(self, spisok, spisok_index, spisok_item):
        self.spisok = spisok
        self.spisok_index = spisok_index
        self.spisok_item = spisok_item

    def dlinaStroka(self):
        return len(self.spisok)

    def get_dlinaStroka(self):
        return self.dlinaSpisok()

    def inStroka(self):
        return (self.spisok_index in self.spisok)

    def get_inStroka(self):
        return self.inSpisok()

    def dobavlenieSpisok(self):
        spisok1 = self.spisok
        spisok1.append(self.spisok_item)
        self.spisok = spisok1
        return self.spisok

    def get_dobavlenieSpisok(self):
        return self.dobavlenieSpisok()

    def __str__(self):
        return f' Длинна списка = {self.spisok} =  {self.dlinaStroka()}\n ' \
               f'Список содержит элемент? "{self.spisok_index}" Ответ: {self.inStroka()}\n' \
               f' В список добовляем элемент {self.spisok_item} получаем новый список {self.dobavlenieSpisok()}'