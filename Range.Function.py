"""Use the range function to print the numbers from 1-20"""
x = range(1,21)
for x in range(1, 21):
    print(x)

"""Repeat the exercise above counting by 2's"""
x = range(1,21)
for x in range(1, 21, 2):
    print(x)



"""Print all the multiples of 5 between 10 and 200 in DECENDING order"""
def five():
    x = 200
    while x > 0:
        if x % 5 == 0:
            print(x)
        x = x - 1
five()
