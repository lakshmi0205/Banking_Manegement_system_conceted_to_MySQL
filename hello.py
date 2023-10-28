
#1 st examples
def hello():
    print("hello world")
hello()

#2nd example
def add(a,b):
    return a+b
k=add(5,6)
print(k)
#3rd examle
def matliple(a,b):
    return a*b
k=matliple(5,6)
print(k)

#4 example
def sub(a,b):
    return a-b
k=sub(5,4)
print(k)
#5th example
def divide(a,b):
    return a/b
k=divide(6,7)
print(k)
#6th example
def modulus(a,b):
    if b!=0:
        return a%b
    else:
        return "can't divided by zero"
    k=modulus(10,3)
print(k)
#7th example
def value(x):
    if x>=0:
        return -x
    else:
        return x
k=value(-2)


#8th quations example
def is_max(a,b):
    return max(a,b)
k=is_max(15,5)
print(k)
#9th quation example
def is_min(a,b):
    return min(a,b)
k=is_min(4,6)
print(k)
#10th example
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
k=factorial(6)
print(k)
#11 th quation
import math
def gcd(a,b):
    return math.gcd(a,b)
k=gcd(12,33)
print(k)
# 12th example
def lcm(a,b):
    return abs(a*b)//gcd(a,b)
k=lcm(12,33)
print(k)

#13th examples
def string_lenght(text):
    return len(text)
length=string_lenght("hello,world")
print(length)
#14th example
def list(lst):
    return len(lst)
length=list([1,2,3,4,5,])
print(length)
#15 example
def sort_list(lst):
    return sorted(lst)
a=sort_list([23,4,5,6])
print(a)
#16 example
def reverse_list(lst):
    return lst[::-1]
a=reverse_list([1,3,4,5,6])
print(a)

#17th example
a=lambda x:x**2
k=a(4)
print(k)
#18th example
add=lambda x,y:x+y
result=add(5,6)
print(result)
#19 th quations
numbers = [1, 2, 3, 4, 5]
squared_numbers = list((lambda x: x ** 2, numbers))
print(squared_numbers)
#20 th quation
num = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print(even_numbers)

