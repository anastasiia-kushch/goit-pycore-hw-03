import re

def normalize_phone(phone_number: str) -> str:
    '''
    Normalizes phone numbers to the standard international format for Ukraine (+38).

    Parameters:
    phone_number (str): a phone number in various formats, which can include spaces, special characters, or different country codes.

    Returns:
    str: the normalized phone number in the format '+38XXXXXXXXXX' (10 digits after the country code).
    '''
    
    pattern = re.compile(r"[+38]?[\d]+")
    res = re.findall(pattern, phone_number)
    res = "".join(res)

    if res.startswith('0'):
        res = '+38' + res
    
    if res.startswith('38'):
        res = '+' + res
    return(res)


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)