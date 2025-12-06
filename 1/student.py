# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.weight = 10

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.weight = 100
    student2.name = "Olivia"
    student2.age = 21
    student2.weight = 60

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, weights {student1.weight} kg')
    print(f'{student2.name}, {student2.age} years old, weights {student2.weight} kg')

if __name__ == "__main__":
    main()