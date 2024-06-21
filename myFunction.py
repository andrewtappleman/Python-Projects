
#Given two integer numbers, return their product only if the
# product is equal to or lower than 1000. Otherwise, return their sum.
def myFunction(a, b):

    # compute product (a * b)
    myProduct = a * b
    mySum = a + b

    # if product <= 1000 return product
    if(myProduct <= 1000):
        answer = myProduct
    else:
        answer = mySum

    return answer

if __name__ == "__main__":

    print(myFunction(20, 30))

    print(myFunction(30, 40))
