weight = input("Your weight is: ")
unit = input("Unit: (K)g (L)bs")

if unit.upper() == "K":
    print("Your weight is " + str(round(float(weight)/0.45, 2)) + "lbs")
else: 
    print("Your weight is " + str(round(float(weight)*0.45, 2)) + "kg")