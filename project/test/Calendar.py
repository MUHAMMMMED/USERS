 

from django.db.models import Count
from django.shortcuts import render
from django.utils.safestring import mark_safe
from itertools import groupby
from calendar import HTMLCalendar
from datetime import datetime, timedelta


class Calendar(HTMLCalendar):
    def __init__(self, know):
        super().__init__()
        self.know = self.group_by_day(know)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if datetime.now().date() == datetime(self.year, self.month, day).date():
                cssclass += ' today'
            if day in self.know:
                cssclass += ' filled'
                body = []
                for item in self.know[day]:
                    body.append(f'<li>{item.title}</li>')
                return f"<td class='{cssclass}'><span class='date'>{day}</span><ul>{''.join(body)}</ul></td>"
            return f"<td class='{cssclass}'><span class='date'>{day}</span></td>"
        return '<td class="noday">&nbsp;</td>'

    def formatweek(self, theweek):
        s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
        return f'<tr>{s}</tr>'



    def formatmonth(self, year, month, withyear=True):
        self.year, self.month = year, month
        v = []
        a = v.append
        a('<table class="calendar">')
        a('\n')
        a(self.formatmonthname(year, month, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(year, month):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return mark_safe(''.join(v))

    def group_by_day(self, know):
        field = lambda know: know.date.day
        return dict(
            [(day, list(items)) for day, items in groupby(know, field)]
        )
 