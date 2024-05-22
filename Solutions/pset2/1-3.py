epilson = 0.01
monthly_interest_rate = annualInterestRate / 12.0
low_bound = balance/12
high_bound = (balance * (1+monthly_interest_rate)**12) / 12.0

while high_bound - low_bound > epilson:
    remaining = balance
    guess = (low_bound+high_bound) / 2.0
    
    for i in range(12):
        remaining = remaining - guess
        remaining = remaining + (remaining * monthly_interest_rate)
        
    
    if remaining > 0:
        low_bound = guess
    elif remaining < 0:
        high_bound = guess
    else:
        break
    
min_monthly_payment = (low_bound + high_bound) / 2
print("Lowest Payment:", round(min_monthly_payment, 2))