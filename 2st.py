import random

def get_numbers_ticket(min, max, quantity):
    if not all(isinstance(i, int) for i in [min, max, quantity]):
        return []

    if not (1 <= min <= max <= 1000) or quantity <= 0:
        return []

    if max - min + 1 < quantity:
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(list(numbers))

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)