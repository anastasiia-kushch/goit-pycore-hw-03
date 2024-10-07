from datetime import datetime

def get_days_from_today(date: str) -> int:

    '''
    Calculates the number of days between today's date and the given date.
    
    Parameters:
    date (str): the date in 'YYYY-MM-DD' format.

    Returns:
    int: the number of days between today and the provided date.

    Raises:
    ValueError: if the input is not a string or if the date format is incorrect.
 
    '''

    if type(date) != str:
        raise ValueError("Incorrect data type. Date should be string")
    
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format. Expected format: YYYY-MM-DD")
    
    current_date = datetime.now().date()
    delta = (current_date - date_obj.date()).days
    return delta

print(get_days_from_today("2021-10-09"))
# print(get_days_from_today("2021/10/09"))