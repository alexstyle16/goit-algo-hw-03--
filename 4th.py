from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            continue

        if birthday > today:
            birthday = birthday.replace(year=today.year - 1)

        days_until_birthday = (today - birthday).days

        if days_until_birthday <= 7:
            if birthday.weekday() in [5, 6]:
                next_weekday = birthday + timedelta(days=(7 - birthday.weekday()))
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": next_weekday.strftime("%Y.%m.%d")})
            else:
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)