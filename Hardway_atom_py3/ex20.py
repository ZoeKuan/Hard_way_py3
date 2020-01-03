from sys import argv

script, input_file =argv

def print_all(f):
    print(f.read())

def rewind(f): #倒帶，變量f要入野入去
    f.seek(0) #去到0（頭）戈個位置

def print_a_line(line_count, f):
    print(line_count, f.readline()) # line_count = current_line

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file) #第1個def(print_all)代替f

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #第2個def(rewind)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += + 1 #自己本身戈個數 ＋1
print_a_line(current_line, current_file)

current_line += + 1
print_a_line(current_line, current_file)
