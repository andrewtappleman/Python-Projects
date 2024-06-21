if __name__ == "__main__":
    singles = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    
    print("singles[:] = ", singles[:])
    print("squares[:] = ", squares[:])
    
    print("squares[:] + [2] = ", squares[:] + [2])
    print("squares[:] + squares[:] = ", squares[:] + squares[:])
    print("squares[:] + singles[:] = ", squares[:] + singles[:])
    print("squares[:] * 2 = ", squares[:] * 2)

    print("squares[3] = ", squares[3])
    squares[3] = 12
    print("squares[3] = ", squares[3])

    singles[1:3] = ['A', 'B']
    print("singles[:] = ", singles[:])

    squares[:] = []
    print("squares[:] = ", squares[:])

    print("list(range(10)) = ", list(range(10)))
    print("list(range(5,10)) = ", list(range(5,10)))
    print("list(range(5,20,2)) = ", list(range(5,20,2)))
    
