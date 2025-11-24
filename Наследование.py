#Наследование
#Пример 1
class Person:
    def __init__(self, name):
        self.__name = name
    def getname(self):
        return self.__name
    def display_info(self):
        print(f"Name: {self.getname()}")
class Employee(Person):
    def __init__(self,name, time):
        super().__init__(name)
        self.__time = time
    def work(self):
        print(f"{self.getname()} works {self.__time}hours")

#Пример 2
class Student:
    def study(self):
        print("Student studies")
class WorkingStudent(Employee, Student):
    pass
#main
def main():
    #Пример1
    # tom = Employee(name="Tom", time=10)
    # tom.work()
    # tom.getname()
    # tom.display_info()

    #Пример 2
    tom = WorkingStudent("Tom")
    tom.work()
    tom.study()


if __name__ == "__main__":
     main()


