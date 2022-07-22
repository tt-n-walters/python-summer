# User input of a number of hours, mintes, and seconds
# And a calculation of the total number of seconds

# 1 hour, 10 minutes, 0 seconds   -> 4200 seconds

print("Enter number of hours:")
hours = input()
hours = int(hours)

print("Enter number of minutes:")
minutes = int(input())

print("Enter number of seconds:")
seconds = input()
seconds = int(seconds)

total = hours * 3600 + minutes * 60 + seconds * 1
print("Total seconds:" + str(total))


# Types in Python
#  str    string        Anything in "quotes"
#  int    integer       Whole numbers
#  float  float         Number with a decimal place
#  bool   boolean       True/False
