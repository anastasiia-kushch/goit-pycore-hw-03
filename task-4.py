from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:

    '''
    Determines upcoming birthdays within the next week (including today) and adjusts for weekends.

    This function processes a list of users and extracts their birthdays,
    checking if any fall within the next 7 days. If a birthday falls on a weekend,
    the congratulation date is moved to the following Monday.

    Parameters:
    users (list): a list of dictionaries, each containing:
        - name (str): the name of the user.
        - birthday (str): the user's birthday in 'YYYY.MM.DD' format.

    Returns:
    list: a list of dictionaries containing:
        - name (str): the name of the user whose birthday is upcoming.
        - congratulation_date (str): the date for congratulations in 'YYYY.MM.DD' format.

    Example:
    >>> users = [
    ...     {"name": "John Doe", "birthday": "1985.10.10"},
    ...     {"name": "Ann Doe", "birthday": "1985.10.12"}
    ... ]
    >>> get_upcoming_birthdays(users)
    [{'name': 'John Doe', 'congratulation_date': '2024.10.10'},
     {'name': 'Ann Doe', 'congratulation_date': '2024.10.14'}]

    '''

    congrats_list = []
    today = datetime.now().date()
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)
            congrats_list.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d") })

    return congrats_list



users = [
    {"name": "John Doe", "birthday": "1985.10.10"},
    {"name": "Ann Doe", "birthday": "1985.10.12"},
    {"name": "Jane Smith", "birthday": "1990.10.15"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)