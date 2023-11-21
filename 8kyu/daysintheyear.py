import calendar
#After finishing this task I will better solution on this task
def year_days(year):
    if year == 0:
        return 365
    elif year < 0:
        days_in_month = [calendar.monthrange(year, month)[1] for month in range(1,13)]
        return sum(days_in_month)
    else:
        days_in_month = [calendar.monthrange(year, month)[1] for month in range(1,13)]
        return sum(days_in_month)


year = int(input())
result = year_days(year)
print(result)
