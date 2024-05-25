username = "desiithoughtss"

#mainly global and function scope

# def func():
#     username = "chai"
#     print(username)
# func()
# print(username)


x = 99
# def func2(y):
#     z = x + y
#     return z
# ans = func2(1)
# print(ans)

# def func3():
#     global x 
#     x = 88
# func3() 
# print(x)

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# ans = f1()
# ans() #bag theory


def chai(num):
    def actual(x):
        return x ** num
    return actual #factory functions
f = chai(2)
g = chai(3)
print(f(3))
print(g(3))