import datetime
if int(datetime.date.today().strftime('%m')) == 12:
    if int(datetime.date.today().strftime('%d')) <= 25:
        print("Christmas")
