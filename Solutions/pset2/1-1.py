remaining = balance
for i in range(12):
    remaining = ( remaining - (remaining*monthlyPaymentRate) )
    interest = remaining * (annualInterestRate/12.0)
    remaining = remaining + interest

print("Remaining balance: ",round(remaining,2))
        