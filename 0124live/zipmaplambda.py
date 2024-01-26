# girls = ['jane', 'ashley', 'kate']
# boys = ['peter', 'jay']
# pair = zip(girls, boys)

# print(list(pair))

def example_func(num1, num2):
    result = num1 + num2
    return result

lst_a = [1, 3, 5]
lst_b = [2, 4, 6]

print(list(map(example_func, lst_a, lst_b)))