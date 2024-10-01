# HOMEWORK - 2nd task
import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int] | str:
    if type(min) is int and type(max) is int and type(quantity) is int:
        if min >= 1 and max <= 1000 and max > min:
            lottery_numbers = sorted(list(set([random.randint(min, max) for i in range(quantity)])))
            return f"Your lottery numbers: {lottery_numbers}" if len(lottery_numbers) == quantity else []
        return (f"Min and max numbers given must be in 1 to 1000 range, and max > min. "
                f"Min equals to {min}, Max to {max}. Enter valid numbers")
    return (f"Wrong input format given: min: {type(min)}, "
            f"max: {type(max)}, quantity: {type(quantity)}. "
            f"Must be min: int, max: int, quantity: int")
