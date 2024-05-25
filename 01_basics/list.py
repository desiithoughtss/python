tea_varities = ["black", "green", "oolong", "ginger"]
print(tea_varities)
#
print(tea_varities[3])
print(tea_varities[-1])
print(tea_varities[1:3])
print(tea_varities[1:])
print(tea_varities[1::2])
#
tea_varities[3] = "Herbal"
print(tea_varities)
#
#tea_varities[1:2] = ["ab"]
#
tea_varities[1:1]= ["test", "test"]
print(tea_varities)
#
tea_varities[1:3] = []
print(tea_varities)
#
for tea in tea_varities:
    print(tea, end="-")
print("")
#
if "green" in tea_varities:
    print("i have green tea")
#  
tea_varities.append("oolong")
print(tea_varities)
#
print(tea_varities.pop())
print(tea_varities)
#
tea_varities.remove("green")
print(tea_varities)
#
tea_varities.insert(1, "green")
print(tea_varities)
#
tea_varities_copy = tea_varities # same reference 
tea_varities_copy = tea_varities.copy() # this is the copy, different referance 
#
tea_varities_copy.append("masala")
print( tea_varities_copy)
#
squared_nums = [x**2 for x in range(1,10)]
print(squared_nums)
#
print("hello", "world", sep="-")