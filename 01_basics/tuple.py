tea_types = ("masala", "green", "oolang")
print(tea_types)
#
print(tea_types[0])
#
# tea_types[0] = "green"  mutable
#
more_tea =("herbal", "early grey")
all_tea = more_tea + tea_types
print(all_tea)
#
if "green" in all_tea:
    print("green tea is present")
#
more_tea = ("herbal"," earl grey", "herbal")
print(more_tea.count("herbal"))
print(more_tea.count("a"))
#
(black, green, oolang) = tea_types
print(black)
print(green)
print(oolang)
print(black, green, oolang) 
#
print(type(tea_types))