def final_deposit_amount(*interest, amount=1000):
    for elem in interest:
        amount *= ((elem / 100) + 1)
    return round(amount, 2)




