num1  = input("enter num1")
num2 = input("enter num2")

isError = False

if num1.isdigit():
    num1 = int(num1)
else:
    isError = True
    print("Please enter numaric value")

if num2.isdigit():
    num2 = int(num2)
else:
    isError = True
    print("Please enter numaric value")

if not isError:
    ans = 1

    for i in range(num2):
        ans = ans * num1

    print(ans)