# class Grandparent:
#     def about(self):
#         print("I'm Grandparent")
#     def about_myself(self):
#         print("I'm Grandparent")
# class Parent(Grandparent):
#     def about(self):
#         print("I'm a Parent")
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
# ch = Child()
# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#     def __init__(self):
#         self.World = "World"
#         self._World = "_World"
#         self.__World = "__World"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.World)
#         print(self._World)
#         print(self.__World)
# class Hi(Hello_world):
#     def hi_printer(self):
#         print(self.hello)
#         print(self._hello)
#         # print(self.__hello)
#         print(self.World)
#         print(self._World)
#         # print(self.__World)
# hello = Hello_world()
# hello.printer()
#
# hi = Hi()
# hi.hi_printer()
# class Class1:
#     var = 20
#     def __int__(self):
#         self.var = 10
# class Class2(Class1):
#     def __int__(self):
#         print(self.var)
#         super().__int__()
#         print(self.var)
#         print(super().var)
#         Class1.var = 50
#         print(super().var)
# obj = Class2()

class Monitor:
    def __init__(self):
        super().__init__()
        self.memory = 128
class Computer:
    def __init__(self):
        super().__init__()
        self.resolution = "4k"
class Smartphone(Monitor, Computer):
    def printer(self):
        print(self.memory)
        print(self.resolution)

iphone = Smartphone()
iphone.printer()
