#1
number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
number_count = 0
for num in number:
    if num > 0:
        number_count = number_count + 1
print(number_count)



#2
number = int(input("enter the nummber: "))
even_sum = 0
for num in range(1,number+1):
    if num % 2 == 0:
        even_sum = even_sum + num
print(even_sum)


#3
table = int(input("enter the number: "))
for num in range(1, 11):
    if num == 5:
        continue
    print( f"{table} * {num} = {num * table}" )



#4
string = input("enter the string: ")
reversed_string = ""
for i in string:
    reversed_string = i + reversed_string
print(reversed_string)



#5
string = "aabbccddeeffghhiijj"
for i in string:
    if string.count(i) == 1:
       print(i)
       break

for i in string:
    if string.count(i) >= 2:
        continue
    else:
        print(i)
        break



#6
number = int(input("enter the number: "))
factorial = 1
while number > 0:
    factorial = factorial * number
    number = number - 1
print(factorial)



#7
while True:
    number = int(input("enter the number: "))
    if number >= 1 and number <= 10:
        print("thanks")
        break
    else:
        print("invalid number")



#8
number = int(input("enter the number: "))
is_prime = True
if number > 1:
    for i in range(2, number):
        if (number %  i) == 0:
            is_prime = False
            break
print(is_prime)



#9
items = ["apple", "banana", "grapes", "mango", "apple", "watermelon"]
unique = set()
for item in items:
    if item in unique:
        print("duplicate")
        break
    else:
        unique.add(item)
print(unique)



#10
import time

wait_time = 1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print(f"Attemps {attempts + 1} - wait time {wait_time}")
    time.sleep(wait_time)
    wait_time *=2 
    attempts += 1