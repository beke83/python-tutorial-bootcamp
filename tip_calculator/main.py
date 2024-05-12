#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was your total bill? $")
percent_tip = input("What percentage tip would you like to give? 10, 20 or 15? ")
num_of_people = input("How many people to split the bill? ")

tip_per_percent = int(percent_tip) / 100 * float(total_bill)
new_total = tip_per_percent + float(total_bill)
total = new_total / int(num_of_people)
total_amount = "{:.2f}".format(total)
print(f"Each person pays: ${total_amount}")



