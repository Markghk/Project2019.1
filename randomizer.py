from random import choice
class Randomizer:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __get_res(self):
        sign = ["+", "-", "*", "/"]
        signs = choice(sign)
        if signs == "+":
            return self.__a + self.__b
        elif signs == "-":
            return self.__a - self.__b
        elif signs == "*":
            return self.__a * self.__b
        elif signs == "/":
            return self.__a / self.__b
    def result(self):
        return self.__get_res()

random_num = Randomizer(5, 10)
print(random_num.result())