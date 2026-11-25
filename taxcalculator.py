def taxable_income(inc):
    return max(inc - 50000, 0)


def tax(inc):
    t = taxable_income(inc)
    if t <= 250000:
        return 0
    elif t <= 500000:
        return (t - 250000) * 5 // 100
    elif t <= 1000000:
        return 12500 + (t - 500000) * 20 // 100
    else:
        return 112500 + (t - 1000000) * 30 // 100


def net_income(inc):
    return inc - tax(inc)


if __name__ == "__main__":
    inc = int(input("Enter your annual income: "))
    print("Taxable income:", taxable_income(inc))
    print("Tax:", tax(inc))
    print("Net income:", net_income(inc))