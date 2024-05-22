payment = 10
while True:
    remaining = balance
    for i in range(12):
        remaining -= payment
        remaining += remaining * (annualInterestRate / 12.0)
    
    if remaining <= 0:
        print("Lowest Payment:", payment)
        break
    else:
        payment += 10