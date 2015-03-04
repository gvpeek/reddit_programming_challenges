from datetime import datetime

input_dates = [ '2015 7 4',
                '2015 10 31',
                '2015 12 24',
                '2016 1 1',
                '2016 2 9',
                '2020 1 1',
                '2020 2 9',
                '2020 3 1',
                '3015 2 9']

def get_days_remaining(date):
    year, month, day = date.split(' ')
    target = datetime(int(year), int(month), int(day), 0, 0)
    return (target - datetime.now()).days

if __name__ == '__main__':
    for date in input_dates:
        print get_days_remaining(date)