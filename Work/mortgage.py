# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108
total_paid = 0.0
month = 0

while principal > 0:
    principal_with_interest = principal * (1 + rate / 12)
    if (principal_with_interest < payment):
        final_payment = principal_with_interest
        principal = 0
        total_paid += final_payment
    else:
        principal = principal_with_interest - payment
        total_paid += payment
    if (month > extra_payment_start_month) and (month <= extra_payment_end_month):
        principal -= extra_payment
        total_paid += extra_payment
    month += 1
    print(month, round(total_paid,2), round(principal, 2))

print("Total paid", total_paid, month)
