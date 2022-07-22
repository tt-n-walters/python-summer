print("Square")
for i in range(7):
    for i in range(7):
        print("*", end=" ")
    print()

print("Rectangle")
for y in range(7):
    for x in range(7):
        if x < 4:
            print("*", end=" ")
    print()


print("Leading triangle")
for y in range(7):
    for x in range(7):
        if x < 7 - y:
            print("*", end=" ")
    print()


print("Leading triangle 2")
for y in range(7):
    for i in range(y):
        print(" ", end=" ")

    for i in range(7 - y):
        print("*", end=" ")

    print()


# print("  " * 1, "* " * 6)
# print("  " * 2, "* " * 5)
# print("  " * 3, "* " * 4)
# print("  " * 4, "* " * 3)
# print("  " * 5, "* " * 2)
# print("  " * 6, "* " * 1)