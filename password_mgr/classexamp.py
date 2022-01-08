#Example 1:
# class student:

#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# class course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_students(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#    
#     def get_avggrade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
#
# s1 = student("niyi",28, 75)
# s2 = student("ope", 27, 95)
# s3 = student("tunde", 25, 90)
#
# c1 = course("science", 2)
#
# c1.add_students(s1)
# c1.add_students(s2)
# c1.add_students(s3)
#
# print(c1.get_avggrade())
#
#===========
# Example 2 with out inheritance
#===========
#
# class dog:

#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def sound(self):
#         print("bark")
#
# class cat:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def sound(self):
#         print("Meow")
#
#=================
# Example 2 with inheritance
#=================
#
class pets:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"my name is {self.name} and i'm {self.age} old")
   
class dog(pets):   
    def __init__(self, name, age, color):
        super().__init__(name, age) # in order to inherit the name and age initialisation from the super class: pets
        self.color = color

    def show(self):
        print(f"my name is {self.name} and i'm {self.age} old with {self.color} color")
   
    def sound(self):
        print("bark")

class cat(pets):
    def sound(self):
        print("Meow")

print(dog("Tim",29,"brown").show())


