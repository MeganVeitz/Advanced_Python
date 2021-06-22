from Ex2_Inheritance import Teacher, Programmer, Nurse


teach1 = Teacher("Meg", "Veitz", 28, "Art", "1")
teach2 = Teacher("Sam", "Wolf", 38, "Geography", "7")
programmer1 = Programmer("Mindy", "Coo", 56, "C++", "JGrasp")
programmer2 = Programmer("Rose", "Hue", 30, "Python", "PyCharm")
nurse1 = Nurse("John", "Roberts", 25, "St. Alexis", "ER")
nurse2 = Nurse("Carl", "Smith", 69, "St. Johns", "VA")

person_list = [
    teach1,
    teach2,
    programmer1,
    programmer2,
    nurse1,
    nurse2
]

for peep in person_list:
    print(peep)
