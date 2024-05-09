#This coding challenge is to calculate a persons Body Mass Index BMI
# The BMI is a measure of someone's weight taking into
# account their height example if a tall person and a short person
# both weigh the same amount, the short person is usually more
# overweight

# The BMI is calculated by dividing a person's weight (in kg) by the square
# of their height

# BMI = weight(kg) / height ** 2 (m)

# Solution
height = input("Enter height: ")
weight = input("Enter weight: ")

weight_as_int = int(weight)
height_as_float = float(height)

# using the exponent operator **
bmi = weight_as_int / height_as_float ** 2

# using bodmas or pemdas
bmi2 = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi)
