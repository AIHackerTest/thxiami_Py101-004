from sys import argv
script, inputfile = argv

def print_all(f):
    s = f.read()
    print(s)
    print('type of text:', type(s))
    print('len of text:', len(s))

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(inputfile)

print("First let's print the whole file:\n")

print_all(current_file)

print("let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines.")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)