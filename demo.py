import random

def reusable_function(arg1, arg2, arg3):
    print("Arg1 = ", arg1)
    print("Arg2 = ", arg2)
    print("Arg3 = ", arg3)

    computation = (arg1 * arg2) + arg3

    return computation


if __name__ == "__main__":
    x = 5
    y = 6
    z = 2

    reusable_function(x, y, z)

    a = random.randint(0, 20)
    b = random.randint(0, 20)
    c = random.randint(0, 20)

    reusable_function(a, b, c)
