# try:
#     a = int(input("A"))
#     b = 10
#     c = b / a
#     print(f"C {c}")
# except ValueError:
#     print("Ви ввели щось не зрозуміле")
# except ZeroDivisionError:
#     print("Ви ввели 0 ")
#     a = 1
#     c = b / a
#     print(f"C {c} and {a}")
# else:
#     print("ELSE")
# finally:
#     print("FINALLY")

# def checker(var):
#     if type(var) != str:
#         raise TypeError(f"Can't work type {type(var)}")
#     else:
#         return ("Ok")
#
# var = "10"
# print(checker(var))

class BuildingError(Exception):
    def __str__(self):
        return "З цею кількістю матеріалів ми не можемо будувати"

    def checker_materials(mater, limit):
        if mater > limit:
            return "Ми будуємо!"
        else:
            raise BuildingError(mater)

        material = 120
        limit = 200

