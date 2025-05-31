

print(type(5))
print(type(5.5))
print(type("ahoj"))

def test():
    return 1

print(type(test))


x = 5

if x == 5:
    print("5")
elif x == 10:
    print("10")
else:
    print("not 5 or 10")


print()
print()

def for_print(xs):
    for x in xs:
        print(x)


def recur_print(xs):
    if len(xs) == 0:
        return
    else:
        print(xs[0])
        recur_print(xs[1:])

def print_only_positive_number(x):
    if x >= 0:
        print(x)
    else:
        raise Exception(f"I print only positive numbers, got: {x}")
    
print_only_positive_number(5)
# print_only_positive_number(-5)

xs = [1, 2, 3, 4, 5]

for_print(xs)
recur_print(xs)


print()
print()

def square(side_len):
    for _ in range(side_len):
        for _ in range(side_len):
            print("*", end = "")
        print()

square(3)


def rectangle(a, b):
    for _ in range(a):
        pass
        
        print()

rectangle(3, 5)
# *****
# *****
# *****

def right_triangle(base_len):
    pass

right_triangle(5)
# *
# **
# ***
# ****
# *****

def triangle(base_len):
    pass

triangle(3)
#  *
# ***

triangle(4)
# throw exception invalid input

triangle(5)
#   *  
#  ***
# *****