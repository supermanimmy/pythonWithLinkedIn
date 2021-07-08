"""Python String Objects"""


print("""
    Hello,
    World. 
    {}
""".swapcase().format(45*5))


class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString("Hello, World.")

print(s)


s1 = 'Hello, World.'
s2 = s1.upper()

# s1 != s2 as the .upper() returns a new string object.
print(id(s1))
print(id(s2))

x = 42
y = 72

"""Formatting String"""
print('The numbers are {xx:<5},{bb:>05}.'.format(xx=x,bb=y))

z = 44*9909

print('The number is {:,}'.format(z).replace(',', '.'))

"""Split and join"""

word = 'This is a long string with a bunch of words in it.'
l = word.split()

word2 = '--'.join(l)
print(word2)