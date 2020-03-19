def calculator(operation_func, operation_name, first_arg, second_arg):
    print("Running " + operation_name + " operation")
    return operation_func(first_arg, second_arg)





def add_operation(a, b):
    return a + b


def subtract_operation(a, b):
    return a - b

def multiply_operation(a, b):
    return a * b

def devide_operation(a, b):
    return a / b


result = calculator(add_operation, "add", 5, 6)
print(result)

result = calculator(subtract_operation, "subract", 5, 6)
print(result)


result = calculator(multiply_operation, "multiply", 5, 6)
print(result)

result = calculator(devide_operation, "devide", 5, 6)
print(result)
