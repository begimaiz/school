class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Teacher(Person):
    def __init__(self, name, age, subjects, experience):
        super().__init__(name, age)
        self.subjects = []
        self.subjects = subjects
        self.experience = experience

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_subject(self):
        return self.subjects

    def add_experience(self, experience):
        self.experience = experience

    def get_experience(self):
        return self.experience


class Student(Person):
    def __init__(self, name, age, group, address):
        super().__init__(name, age)
        self.group = group
        self.address = address

    def set_group(self, group):
        self.group = group

    def get_group(self):
        return self.group

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

def add_data():
    teachers = {}
    Teacher1 = Teacher('Svetlana Genadyevna', 67, 'History', 30)
    Teacher1.set_name('Sveta Gena')
    teachers[0] = Teacher1
    Teacher2 = Teacher('Haci Karaduman', 60, 'Physics', 20)
    teachers[1] = Teacher2

    for i in teachers.keys():
        print(teachers[i].get_name())
        print(teachers[i].get_subject())

    students = {}
    Student1 = Student('Begimai Zulpukarova', 28, 11, 'Kievskaya street 76')
    Student2 = Student('CHondoloeva Izat', 29, 11, 'Gogolya street')
    students[0] = Student1
    students[1] = Student2

    for i in students.keys():
        print(students[i].get_name())
        print(students[i].get_address())

add_data()