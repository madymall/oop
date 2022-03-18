staging = True
message = 'Hello, it\'s const in my_module.py!'

def get_sum(num1=None, num2=None, array = None):
    if array:
        return sum(array)

    return num1 + num2