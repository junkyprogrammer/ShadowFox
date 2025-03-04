#In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π)
# defining a variable for circular pond


crcpnd = 84

# Using its formula Circle Area = pi*r*r

area=(3.14*crcpnd*crcpnd)

# printing it's result 

print("Area of the circular pond of radius 84 Meters is : ", area,"m^2")

#Bonus Question
#If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it.

totalWater = (1.4*area)

#Converting float value into integer value

constValue = int(totalWater)

#Printing the result of the Bonus Ques

print("Total Amount of water in that pond is : ",constValue , "ltr (Approx)")
