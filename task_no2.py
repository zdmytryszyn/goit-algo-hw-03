# HOMEWORK - 2nd task
import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int] | str
    if 1 <= min < max <= 1000 and (max - min) >= quantity:
        lottery_numbers = sorted(set([random.randint(min, max) for i in range(quantity)]))
        return lottery_numbers if len(lottery_numbers) == quantity \
            else get_numbers_ticket(min, max, quantity)
    return []
