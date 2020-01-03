from sys import argv

script, input_num = argv

i = 0
numbers = []

while i < eval(input_num): #eval() 函数用来执行一个字符串表达式，并返回表达式的值。eval(expression[, globals[, locals]])
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
