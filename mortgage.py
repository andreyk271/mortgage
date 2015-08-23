total_sum = 200000
monthly_payment = 1000
overpayment = 500

def calc(total_sum, percent_annually, monthly_payment, overpayment, period_years, fees):
    percent_payment_total = fees
    for i in range(period_years * 12):
        percent_payment = total_sum / 100 * percent_annually / 12
        percent_payment_total += percent_payment
        total_sum -= monthly_payment + overpayment - percent_payment
    print(total_sum, percent_payment_total)

# years, percent with 999 fee, percent without fee
mortgages = [
    (2, 1.74, 2.04),
    (3, 2.29, 2.59),
    (4, 2.44, 2.69),
    (5, 2.64, 2.79),
    (10, 3.24, 3.34)
]

for m in mortgages:
  calc(total_sum, m[1], monthly_payment, overpayment, 2, 999)
  calc(total_sum, m[2], monthly_payment, overpayment, 2, 0)
