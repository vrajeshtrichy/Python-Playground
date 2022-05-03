class Heart:
    def __init__(self, heartValves):
        self.heartValves = heartValves

    def display(self):
        return self.heartValves

class Person:
    def __init__(self, fname, lname, address, heartValves, heart):
        self.fname = fname

        # _lname is protected instance variable
        self._lname = lname

        # __address is private instance variable
        self.__address = address
        # Composition
        self.heartObject = Heart(heartValves)

        # Aggregation
        self.heartValves = heart

    def display(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self._lname)
        print("Address: ", self.__address)

    # Deleting (Calling destructor)
    def __del__(self):
        print('\nDestructor called, Person deleted.')


class Student(Person):
    def __init__(self, fname, lname, address, heartValves, heart, age, gradYear):
        super().__init__(fname, lname, address, heartValves, heart)
        self.age = age
        self.gradYear = gradYear

    def display(self):
        super().display()
        print("Age: ", self.age)
        print("Graduation Year: ", self.gradYear)
        print("Graduation Year: ", self._lname)

# person object
hv = Heart(4)
per = Person("Adam", "Ho", "1234 abc blvd", 4, hv)
per.display()
print("===========================================")
std = Student("Peter", "kee", "9876 xyz blvd", 4, hv, 28, 2008)
std.display()

print(per._lname)
