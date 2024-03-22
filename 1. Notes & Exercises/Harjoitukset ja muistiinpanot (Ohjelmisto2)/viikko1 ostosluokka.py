
'''
class Ostoslista:
    def __init__(self, lista):
        self.lista = lista

lista1 = Ostoslista("maito", "leipä", "juusto")
print(lista1.lista)
'''
'''
# ----------------------------------------------------------------
class School:
    def __init__(self, name):
        self.name = name

school1 = School("Kumpulan koulu")
school2 = School("Käpylän koulu")


class Students:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        

student1 = Students("Pekka", school1)
student2 = Students("Maija", school2)


print(f"'{student1.name}' opiskelee paikassa: '{student1.school.name}'.")
print(f"'{student2.name}' opiskelee paikassa: '{student2.school.name}'.")

'''

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

book1 = Book("Python 101")
book2 = Book("Pelle Miljoona")
book3 = Book("Koirien elämää")

library1 = Library("Kallion kirjasto")
library2 = Library("Käpylän kirjasto")

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)

library2.add_book(book1)
library2.add_book(book2)


print (f"\n'{library1.name}' sisältää kirjat:")
for book in library1.books:
    print(book.title)

print (f"\n'{library2.name}' sisältää kirjat:")
for book in library2.books:
    print(book.title)