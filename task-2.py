import random

def args_check(min, max, quantity):
    if min < 0 or max < 0 or quantity < 0:
        raise Exception ("Min, max, and quantity must not be negative.")

    if min < 1:
        raise Exception('Min must be at least 1.')
    
    if max > 1000:
        raise Exception('Max must not exceed 1000.')
    
    if quantity >= max:
        raise Exception('Quantity must be between min and max.')


def get_numbers_ticket(min, max, quantity):

    args_check(min, max, quantity)
    
    set_of_numbers = set()

    while len(set_of_numbers) < quantity:
        res = random.randrange(min, max)
        set_of_numbers.add(res)

    list_of_numbers = list(set_of_numbers)

    return sorted(list_of_numbers)


print(get_numbers_ticket(0, 100, 4))
