def calculate_total(prices, discount_percent=0):
    subtotal = sum(prices)
    discount_amount = (subtotal * discount_percent) / 100
    final_total = subtotal - discount_amount

    return {
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "final_total": final_total,
    }


if __name__ == "__main__":
    prices = [50, 30, 45, 25]
    print(calculate_total(prices))
    print(calculate_total(prices, 10))
    print(calculate_total(prices, 20))
