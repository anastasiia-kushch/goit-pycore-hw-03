import random

def args_check(min, max, quantity):
    '''
    Validates the input parameters for generating the lottery ticket.

    Raises:
    Exception: if min, max, and quantity are negative.
    Exception: if min is less than 1.
    Exception: if max is more than 1000.
    Exception: if quantity is more than difference between min and max.
    '''
    if min < 0 or max < 0 or quantity < 0:
        raise Exception ("Min, max, and quantity must not be negative.")

    if min < 1:
        raise Exception('Min must be at least 1.')
    
    if max > 1000:
        raise Exception('Max must not exceed 1000.')
    
    if quantity >= max - min:
        raise Exception('Quantity must be less than the difference between max and min.')


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    '''
    Generates a set of unique random numbers for a lottery ticket.
    
    Parameters:
    min (int): the minimum possible number in the set (at least 1).
    max (int): the maximum possible number in the set (no more than 1000).
    quantity (int): the number of numbers to be selected (value between min and max).

    Returns:
    list: a sorted list of unique, randomly selected numbers.

    Raises:
    Exception: if any of the conditions regarding min, max, and quantity are violated.
    '''

    args_check(min, max, quantity)
    
    set_of_numbers = set()

    while len(set_of_numbers) < quantity:
        res = random.randrange(min, max)
        set_of_numbers.add(res)

    list_of_numbers = list(set_of_numbers)

    return sorted(list_of_numbers)


print(get_numbers_ticket(5, 8, 2))
