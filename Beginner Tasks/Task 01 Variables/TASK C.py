#Task C
#Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. 
#Formula: Simple Interest = P x R x T / 100

prncplamt =float(input("Please enter the Principal Amount : "))
rateOfint = float(input("Please input the applicable rate of interest : "))
time = int(input("Please enter the duration of the Loan to calculate the Interest Amount : "))

simplint = (prncplamt * rateOfint * time)/100

print("Simple Interest Amount applicable for the current loan is : ", simplint)
