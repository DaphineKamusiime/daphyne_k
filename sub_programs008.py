#function that converts fahrenheit temperature to celsius
fahren_temp=float(input("Enter fahrenheit temperature: "))
#converting to celcius
#9C+160=5F
celcius_temp=(((5*fahren_temp)-160)/9)
print(round(celcius_temp,4))

