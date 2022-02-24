mylist = [-1, -2, 3, -4, -5]
mylist = list(map(lambda x: -x, mylist))  # Or "lambda x: x*-1"
print(mylist)  # [-1, -2, -3, -4, -5]