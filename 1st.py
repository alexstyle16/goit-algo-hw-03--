from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        difference = date_obj - today  # помилка тут, має бути today - date_obj
        return difference.days  # помилка тут, має бути today.days
    except ValueError:
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."

print(get_days_from_today("2021-10-09"))