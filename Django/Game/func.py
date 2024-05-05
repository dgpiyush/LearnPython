def add_nums(*args,**kwargs):
    print(kwargs)
    print(args)
    return 'kwargs'


print(add_nums(23,id=4, name='test'))


# args is a tuple  and it should come first in the function definition
# kwargs is a dictionary and it should come last in the function definition