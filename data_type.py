'''a=10
b=20
c=6+2j
s='hi i am ani and doing python'
print(a,(type(a)))
print (type(a))
print(b)
print(type(b))
print(c)
print(c.real)
print(c.imag)
print(type(c))
print(s)
print(type(s))

bool=True
print(type(b))
print(b)
f=5.5
print(f)'''


import string
 
 
def remove(string):
    return string.translate(None, ' \n\t\r')
 
 
# Driver Program
string = ' g e e k '
print(remove(string))