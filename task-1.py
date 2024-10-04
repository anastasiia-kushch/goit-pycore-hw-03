from datetime import datetime

def get_days_from_today(date):

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