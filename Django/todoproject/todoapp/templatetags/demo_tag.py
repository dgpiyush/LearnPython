from django import template
register = template.Library()




def demo(value, arg):
    print(value, arg)
    return value.replace(arg, "")



register.filter("demo", demo)