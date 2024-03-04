# Simple Interest Calculator
P = float(input('Please enter Principal (INR) : '))
N = float(input('Please enter Period in Years : '))
R = float(input('Please enter Rate of Interest in %p.a.'))

# calculating simple interest
I =(P*N*R/100)

# calculating the amount
A = P + I

# Print the results
print(f'Simple Interest is : {I:.2f} INR')
print(f'Total Amount : {A:.2f} INR')