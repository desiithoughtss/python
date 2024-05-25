#1
# def square_num(n): #parameters(placeholders)
#     return n**2
# ans = square_num(9)
# print(ans) #arguments



#2
# def value_sum(num1, num2):
#     return num1 + num2
# ans = value_sum(1,8)
# print(ans)



#3
# def multiply(num1 , num2):
#     return num1*num2
# ans1 = multiply(1, 9)
# print(ans1)
# ans2 = multiply("abc", 3)
# print(ans2)



#4
# import math
# def func(radius):
#     area = (math.pi * (radius**2) ) 
#     circum = (2 * math.pi * radius)
#     return area, circum
# ans = func(9)
# print(ans)



#5
# name = input("enter your name: ")
# def greet_user(name):
#     if name == "":
#         return "hello desiithoughtss"
#     elif name != "":
#         return f"hello {name}"
# ans = greet_user(name)
# print(ans)



#6
# cube = lambda x: x**3
# print(cube(3))



#7
# def sum_all(*args):
#     print(args)
#     print(*args)
#     for i in args:
#         print(i * 2)
#     return sum(args)
# print(sum_all(1,2,3))



#8
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_kwargs(name = "akshit", page = "desiithoughtss") 



#9
limit = int(input("enter the number: "))
def even_num(n):
    even_arr = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_arr.append(i)
    return even_arr
ans = even_num(limit)
print(ans)

limit = int(input("enter the number: "))
def even_num(n):
    even_arr = []
    for i in range(2, n+1, 2):
        even_arr.append(i)
    return even_arr
ans = even_num(limit)
print(ans)

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i
for num in even_generator(10):
    print(num)



#10
num =5
fact = 1
while num > 0:
    fact= fact* num
    num = num -1
print(fact)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
ans = factorial(5)
print(ans)

