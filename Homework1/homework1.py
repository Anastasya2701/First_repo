import datetime

def get_days_from_today(date_str):
    try:
            datetime_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            current_day: datetime.datetime = datetime.datetime.today()
            differens = datetime_object - current_day
            return differens.days
    except ValueError:
          return "Неправельний формат дати. Введіть дату у форматі 'YY-MM-DD'."


print(get_days_from_today("2020-10-09"))  