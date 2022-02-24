from functools import reduce
 num_list = [1,2,3,4,5]
 def prod(x, y):
     return x * y
 product = reduce(prod, num_list)
 print(product)
