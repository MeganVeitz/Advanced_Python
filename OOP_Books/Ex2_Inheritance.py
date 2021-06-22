class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def do_work(self):
        print("I'm person {} {}, I'm {} years old and I'm doing work".format(self.first_name, self.last_name, self.age))


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject, grade_level):
        super(Teacher, self).__init__(first_name, last_name, age)
        self.subject = subject
        self.grade_level = grade_level

    def do_work(self):
        print("I'm a teacher and I teach {} grade {}.".format(self.grade_level, self.subject))

    def __str__(self):
        return "I'm teacher {} {}, I'm {} years old and I teach {} grade {} class".format(self.first_name, self.last_name, self.age, self.grade_level, self.subject)


class Programmer(Person):
    def __init__(self, first_name, last_name, age, specialty, preferred_ide):
        super(Programmer, self).__init__(first_name, last_name, age)
        self.specialty = specialty
        self.preferred_ide = preferred_ide

    def do_work(self):
        print("I'm a programmer and my specialty is {} and my preferred ide is {}".format(self.specialty, self.preferred_ide))

    def __str__(self):
        return "I'm programmer {} {}, I'm {} years old and I code in {} and I prefer {}".format(self.first_name, self.last_name, self.age, self.specialty, self.preferred_ide)


class Nurse(Person):
    def __init__(self, first_name, last_name, age, hospital, department):
        super(Nurse, self).__init__(first_name, last_name, age)
        self.hospital = hospital
        self.department = department

    def __str__(self):
        return "I'm nurse {} {}, I'm {} years old and I'm at hospital {} and in department {}".format(self.first_name, self.last_name, self.age, self.hospital, self.department)
