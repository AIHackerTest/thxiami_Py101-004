the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count: {number}")
    
# same as above
for fruit in fruits:
    print("A fruit of type: {fruit}")
    
# also we can go through mixed lists too
# notice we have to use {!r} since we don't know what's in it
for i in change:
    print(f"I got {i!r}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
"""
在 Python 2 中， range() 函数返回一个 list， 初始化时会分配内存地址
在 Python 3 中, range() 函数返回一个序列对象, 初始化时并不会分配内存地址，根据需要返回整数，
若需要一个列表，使用list(range(1,5)) 即可 
"""
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand.
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print(f"Element was: {i}")