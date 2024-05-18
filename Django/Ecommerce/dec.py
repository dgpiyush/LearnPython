def divideDec(func):

    def wrapper(num1,num2):
        if num2 == 0:
            print("num2 can't be zero")
            return
        func(num1, num2)

    return wrapper
 
@divideDec
def twodivide(num1, num2):
    print(num1/num2)



# twodivide = divideDec(twodivide)

twodivide(4,0)



