
class Ostoslista:
    def __init__(self, lista):
        self.lista = lista

lista1 = Ostoslista("maito", "leipä", "juusto")
print(lista1.lista)

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


class Student:
    Student_list = []

    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self,course):
        self.courses.append(course)
        course.students.append(self)
        


class Course:

    def __init__(self, name):
        self.name = name
        self.students = []
    
student1 = Student("Pekka")
student2 = Student("Maija")
course1 = Course("Python 101")
course2 = Course("Javascript 101")

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course2)


print(f"\n'{student1.name}' opiskelee kursseja:")
for course in student1.courses:
    print(course.name)

print(f"\n'{student2.name}' opiskelee kursseja:")
for course in student2.courses:
    print(course.name)

print(f"\n'{course1.name}' kurssilla opiskelee:")
for student in course1.students:
    print(student.name)

print(f"\n'{course2.name}' kurssilla opiskelee:")
for student in course2.students:
    print(student.name)



class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Hoitola:
    def __init__(self):
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        print(koira.nimi + " kirjattu sisään")
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(koira.nimi + " kirjattu ulos")
        return

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)

# Pääohjelma

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()

hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)
hoitola.tervehdi_koiria()

hoitola.koira_ulos(koira1)
hoitola.tervehdi_koiria()



class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self): # sama metodi eri eläimillä
        print("Animal is making a sound")

class Dog(Animal):
    def __init__ (self, species, breed):
        self.breed = breed
        super().__init__(species)

    def speak(self): # sama metodi eri eläimillä uudestaan, periytyy
        print("Dog is barking")

dog1 = Dog("Dog", "Labrador")
dog1.speak()


class Henkilö:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä

    def esittely(self):
        print(f"\nHei, olen {self.nimi} ja olen {self.ikä} vuotta vanha.\n")

class Opiskelija(Henkilö):
    def __init__(self, nimi, ikä, opiskelijanumero):
        self.opiskelijanumero = opiskelijanumero
        super().__init__(nimi, ikä)

    def esittely(self):
        super().esittely()
        print(f"My student number is '{self.opiskelijanumero}'\n")

opiskelija1 = Opiskelija("Rene", 7, 123456789)

opiskelija1.esittely()
 


class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kuukausipalkka: {self.kuukausipalkka}")


työntekijät = []
työntekijät.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
työntekijät.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
työntekijät.append(Työntekijä("Pekka", "Puro"))
työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

for t in työntekijät:
    t.tulosta_tiedot()
