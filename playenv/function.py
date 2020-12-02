def student(name, age, **marks):
    print("name: ", name)
    print("age: ", age)
    print("marks: ", marks)
    for key,value in marks.items():
        print(key, ' ', value)

student('tom', 66, en=99, lt=77, ru=44)    