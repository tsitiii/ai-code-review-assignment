# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values: list) -> float:
    ''' if input isnot type list it should return early'''
    if not isinstance(values, list):
        return 0
    total = 0
    count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (TypeError, ValueError):
                continue

    if count == 0:
        return 0

    return total / count
