total_sum = 200000
monthly_payment = 1000
overpayment = 500

def calc(total_sum, percent_annually, monthly_payment, overpayment, period_years, fees, years):
    percent_payment_total = fees
    for i in range(period_years * 12):
        percent_payment = total_sum / 100 * percent_annually / 12
        percent_payment_total += percent_payment
        total_sum -= monthly_payment + overpayment - percent_payment
    print( total_sum, percent_payment_total)

calc (total_sum, 1.74, 912.34, overpayment, 2, 999, 2)
calc (total_sum, 2.04, 940.88, overpayment, 2, 0, 2)
calc (total_sum, 2.29, 965.07, overpayment, 2, 999, 3)
calc (total_sum, 2.59, 994.59, overpayment, 2, 0, 3)
calc (total_sum, 2.44, 979.76, overpayment, 2, 999, 4)
calc (total_sum, 2.69, 1004.54, overpayment, 2, 0, 4)
calc (total_sum, 2.64, 999.56, overpayment, 2, 999, 5)
calc (total_sum, 2.79, 1014.56, overpayment, 2, 0, 5)
calc (total_sum, 3.24, 1060.36, overpayment, 2, 999, 10)
calc (total_sum, 3.34, 1070.70, overpayment, 2, 0, 10)

