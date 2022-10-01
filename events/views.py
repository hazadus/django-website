from django.shortcuts import render
import calendar
from calendar import HTMLCalendar


def home(request, year=2022, month='October'):
    month = month.title()
    month_number = list(calendar.month_name).index(month)

    clndr = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 'home.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'clndr': clndr
    })
