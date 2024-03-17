

try:
    # FileNotFoundError
    with open('demo.txt') as f:
        data = f.read()
        print(data)
    # ZeroDivisionError
    # x = 5/0
    # valueError
    raise ValueError("invalid value")

except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print(e, 'you cannot divide by zero')


print("programe is running")