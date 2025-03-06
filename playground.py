# *args: many positional arguements
# def add(*args):
#     print(args[1])
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)

# print(add(3, 5, 6, 2, 1, 7, 4, 3))

# **kwargs: many keyword arguements

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)

    

    



calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.makr = kw.get("make")
        self.model = kw.get("model")
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)