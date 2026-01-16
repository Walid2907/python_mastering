#let's convert the weight that u need from kg to pound or pound to kg
weight = float(input("entre the weight you want to convert: "))
unit = input("kilograms or pounds (kg or lbs): ")
if unit == "kg":
    print(f"the weight converted to pounds is {round(weight * 2.205, 2)} lbs")
elif unit == "lbs":
    print(f"the weight converted to kilograms is {round(weight / 2.205, 2)} kg")
else:
    print("the unit is wrong")