def perimeterRect(a1, a2):
    return ((2*a1) + (2*a2))

def perimeterSquare(length):
    return perimeterRect(length, length)

def perimeterCircle1(radius):
    answer = 2 * 3.1415926 * radius
    return answer

def areaCircle(radius):
    return 3.14 * radius * radius

def func(x):
    print("input argument is ", x)
    answer = (2*x) + 4
    print("the answer is ", answer)
    return answer

# this function takes 3 numbers, and returns their sum
def SethsSumThreeNumbers(a, b, c):
    answer = a + b + c
    return answer

# this function take 2 numbers and returns their difference
def difference(num1, num2):
    answer = num1 - num2
    return answer

def score(segment, ring):
    return (segment * 0.1) + (5- ring)*50

if __name__ == "__main__":

    l = 3
    w = 5
    r = 2.5

    print(l, "x", w, " rect perimeter = ", perimeterRect(l, w))
    print(l, "x", l, " square perimeter = ", perimeterSquare(l))
    print("radius ", r, " circle perimeter = ", perimeterCircle1(r))

    print(SethsSumThreeNumbers(4, 6, 8)) # 4 + 6 + 8 = 18
    print(SethsSumThreeNumbers(1, 2, 3)) # 1 + 2 + 3 = 6
    print(SethsSumThreeNumbers(4353, 326, -7890))

    print(difference(27, 28 )) # should be -1
    print(difference(SethsSumThreeNumbers(4, 6, 8), SethsSumThreeNumbers(1, 2, 3)))

    print("Andrew's score ", score(20, 3))
    print("Benjamin's score ", score(11, 1))
    print("Priya's scores ", score(19, 2))
    

    #y = func(4)
    #print(y)
    #func(2)
    #func(-1)



    # f(x) = 2*x + 4

    # f(4) = 5*4 = 20

    
