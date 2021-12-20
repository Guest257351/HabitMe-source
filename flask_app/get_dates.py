from datetime import date, timedelta, datetime
import calendar

def all_dates_current_month():
    month = datetime.now().month
    year = datetime.now().year
    number_of_days = calendar.monthrange(year, month)[1]
    first_date = date(year, month, 1)
    last_date = date(year, month, number_of_days)
    delta = last_date - first_date

    return [(first_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]


# function to take a list of dates and an event to put in all the dates and return a list of dictionaries with the date and the event
def add_event_to_dates(dates, event):
    date_event_list = []
    for date in dates:
        date_event_list.append({'date': date, 'todo': event})
    return date_event_list