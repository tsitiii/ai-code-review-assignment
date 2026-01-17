# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders: list[dict]) -> float:
    total = 0
    count = 0

    for order in orders:
        if order.get("status", "").lower() != "cancelled":
            amount = order.get("amount", 0)
            try:
                amount = float(amount)
            except (TypeError, ValueError):
                continue
            if amount != 0:
                total += amount
                count += 1

    if count == 0:
        return 0

    return total / count
