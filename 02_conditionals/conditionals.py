#1 
age = int(input("enter your age: "))
if age < 13:
    print("child")
elif age < 20:
    print("teenage")
elif age < 60:
    print("adult")
else:
    print("senior")


  
#2
age = int(input("Enter your age: "))
day = input("enter day:  ")
if day.lower() == "wednesday":
    if age < 18:
        print("price is $6")
    else:
        print("price is $10")
else:
    if age < 18:
        print("price is $8")
    else:
        print("price is $12")

age = int(input("Enter your age: "))
day = input("Enter day: ").strip().lower()
if day == "wednesday":
    price = 6 if age < 18 else 10
else:
    price = 8 if age < 18 else 12
print(f"Price is ${price}")



#3
score = int(input("enter your score: "))
if score >= 101:
    print("please enter your correct marks")
    exit()
if score >= 90 and score <=100:
    print("A")
elif score>= 80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
    
    

#4 
color = input("enter the color: ").strip().lower()
if color == "green":
    print("unripe")
elif color == "yellow":
    print("ripe")
elif color == "brown":
    print("overripe")
else: 
    print("enter the valid color")



#5
weather = input("enter the weather: ").strip().lower()
if weather == "sunny":
    print("go out for the walk")
elif weather == "rainy":
    print("read a book")
if weather == "snowy":
    print("build a snowman")
else:
    print("enter the valid weather")



#6
distance = int(input("enter the distance: "))
if distance < 3:
    print("walk")
elif distance <=15:
    print("bike")
else:
    print("car")



#7
order = input("do you want the order: ").strip().lower()
coffe_size = None
if order == "no":
    print("ok")
    exit()
else:
    coffe_size = input("tell me your order size: ").strip().upper()
    extra_shot= input("do you need extra shot: ").strip().lower()
    if extra_shot == "yes":
        print( coffe_size + " with extra shot" )
    else:
        print( coffe_size + "without extra_shot" )



#8
pass_length = int(input("enter the length of password: "))
if pass_length < 6:
    print("weak")
elif pass_length <= 10:
    print("medium")
else:
    print("strong")



#9
year = int(input("enter the year: "))
if year % 400 == 0:
    print("leap year")
else:
    if year % 4 == 0:
        if year % 100 != 0:
            print("leap year")
    else:
        print("not a leap year")
        
year = int(input("Enter the year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
