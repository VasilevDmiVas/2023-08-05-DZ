from classes.Stroka import Stroka
from classes.Spisok import Spisok

def dlinaS(some_objekt):
    return some_objekt.dlinaStroka()

def inStrokaS(some_objekt):
    return some_objekt.inStroka()

def zamenaStroka(some_objekt):
    return some_objekt.zamenaStroka()

def dobavlenieSpisok(some_objekt):
    return some_objekt.dobavlenieSpisok()

stroka = Stroka('Privet mir', 'p', 'P', 'D')
spisok = Spisok(['Привет мир', 12, 15, 'Мир рухнул'], 12, 1)

print(spisok)
print('--------------------------------------------------------------------------------------------------------')
print(stroka)
# print(dlinaS(spisok))
# print(inStrokaS(spisok))
# print(zamenaStroka(stroka))


