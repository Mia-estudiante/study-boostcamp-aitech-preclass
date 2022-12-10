class Person(object): # object 지정 안 해줘도 기본으로 이를 상속받음
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return "저의 이름은 {0}입니다. 나이는 {1}입니다."\
        .format(self.name, self.age)

class Korean(Person):
    pass

first_korean = Korean("철수", 35)
print(first_korean)