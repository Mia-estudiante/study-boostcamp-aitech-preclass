class Person(object): # object 지정 안 해줘도 기본으로 이를 상속받음
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "저의 이름은 {0}입니다. 나이는 {1}입니다."\
        .format(self.name, self.age)

    def about_me(self):
        return "저의 이름은 {0}입니다. 나이는 {1}입니다."\
        .format(self.name, self.age)


class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date
    
    def do_work(self):
        print("열심히 일을 합니다.")

    def about_me(self):
        super().about_me()
        print("제 급여는", self.salary, "원 이고요, 제 입사일은", self.hire_date,\
        "입니다.")

myPerson = Person("John", 34, "Male")
myEmployee = Employee("Daeho", 34, "Male", 300000, "2012/03/01")
myEmployee.about_me()