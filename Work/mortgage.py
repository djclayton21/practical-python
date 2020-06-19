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
    if principal_with_interest < payment:
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
    result = f"{month:<3}{total_paid:12.2f}{principal:12.2f}"
    print(result)

summary = f'Paid ${round(total_paid,2)} total in {round(month/12)} years and {month % 12} months'
print(summary)
