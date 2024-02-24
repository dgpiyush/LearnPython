def left_triangle1(row):

    for i in range(1, row+1):
        # star
        for j in range(i):
            print("*",  end="")
        # next line 
        print()

def left_triangle2(row):
    for i in range(row, 0 , -1):
        # star
        for j in range(i):
            print("*",  end="")
        
        # next line 
        print()

def right_triangle1(row):
    for i in range(1, row+1):

        # space
        for j in range(row-i):
            print(" ", end=" ")
        
        # star
        for k in range(i):
            print("*", end = " ")
        

        # next line 
        
        print()

def right_triangle2(row):
    for i in range(row, 0, -1):
        # space
        for j in range(row-i+1):
            print(" ", end=" ")
        
        # star
        for k in range(i):
            print("*", end = " ")
        
        # next line 
        
        print()

def pyramid(row):
    for i in range(1, row+1): 
        # space
        for k in range(row-i):
            print(" ", end="")
        # star
        for j in range(i):
            print("*", end=" ")
        # next line
        print()

def hollow_square(row):
    for i in range(1, row+1):
        for j in range(1, row+1):
            if i == 1 or i == 5 or j == 1 or j == 5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        print()

def square(row):
    for i in range(1, row+1):
        for j in range(1, row+1):
            print("*", end=" ")
      
        
        print()

def left_triangle3(row):
    left_triangle1(row)
    left_triangle2(row-1)

def right_triangle3(row):
    right_triangle1(row)
    right_triangle2(row-1)




