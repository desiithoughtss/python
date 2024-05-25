#
chai = "masala chai"
print(chai.find("chai"))
print(chai.find("Chai"))
#
chai = "masala chai chai chai"
print(chai.count("chai"))

#
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))

#
chai_variety = ["mint", "masala", "ginger"]
print(" ".join(chai_variety))

#
chai = "Masala chai"
print(len(chai))

#
for letter in chai:
    print(letter)
    
#
chai = "he said, \"Masala chai is awesome\" "
print(chai)

#
chai = "masala chai"
print("masala" in chai)

