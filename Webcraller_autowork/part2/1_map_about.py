# map 함수에 대하여

lst = [2, 3, 4, 5, 6]

def add(x):
    return x + 1

result = list(map(add, lst))
print(result)