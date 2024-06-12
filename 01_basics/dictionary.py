chai_types = {"masala": "spicy chai", "ginger": "zesty chai", "green": "mild chai"}
print(chai_types)
#
print(chai_types["masala"])
#
print(chai_types.get("ginger"))
print(chai_types.get("any"))
#
chai_types["green"] = "fresh"
print(chai_types)
#
for chai in chai_types:
    print(chai) # key print hoti hai
#    
for chai in chai_types:
    print(chai, "->" ,chai_types[chai])
 #   
for key, values in chai_types.items():
    print(key, values)
#
if "masala" in chai_types:
    print("masala tea is present")
#
print(len(chai_types)) # item -> (key + values)
#
chai_types["milk tea"] = "apni pasand"
print(chai_types)
#
chai_types.pop("ginger")
print(chai_types)
#
print(chai_types.popitem())
print(chai_types)
#
del chai_types["green"]
print(chai_types)
#
chai_types_copy = chai_types.copy()
#
tea_shop = {
    "chai":{
    "masala": "spicy", 
    "ginger" : "zesty" 
    },
    "tea" : {
        "green": "mild",
        "black": "strong"
    }
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["masala"])
#
squared_nums = {x:x**2 for x in range(1, 10)}
print(squared_nums)
#
squared_nums.clear()
print(squared_nums)
#
keys = ["masala", "ginger", "green"]
default_value = "delicious"
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)