import datetime

Days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

print('''CALENDAR MAKER.
Creates monthly calendars, saved to a text file and fit for printing.''')

while True:
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response):
        year = int(response)
        break

    print('Please enter a numeric value for the year, like 2023.')
    continue

while True:
    print('Enter a month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Enter a numeric value for the month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def get_calendar(year, month):
    cal_text = ''

    cal_text += (' ' * 57) + Months[month - 1] + ' ' + str(year) + '\n'
    cal_text += ('.' * 6) + 'SUNDAY' + ('.' * 11) + 'MONDAY' + ('.' * 11) + 'TUESDAY' + ('.' * 11) + 'WEDNESDAY' + ('.' * 11) + 'THURSDAY' + ('.' * 11) + 'FRIDAY' + \
        ('.' * 11) + 'SATURDAY' + ('.' * 5) + '\n'

    week_seperator = ('+-----------------' * 7) + '+\n'

    blank_row = ('|                 ' * 7) + '|\n'

    current_date = datetime.date(year, month, 1)

    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_seperator

        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)

            if current_date.month == 12 and current_date.day == 25:
                day_number_row += '|' + day_number_label + ' CHRISTMAS DAY' + (' ' * 1)
            elif current_date.month == 12 and current_date.day == 26:
                day_number_row += '|' + day_number_label + ' BOXING DAY' + (' ' * 4)
            elif current_date.month == 12 and current_date.day == 31:
                day_number_row += '|' + day_number_label + " NEW YEAR'S EVE"
            elif current_date.month == 1 and current_date.day == 1:
                day_number_row += '|' + day_number_label + " NEW YEAR'S DAY"
            elif current_date.month == 5 and current_date.day == 1:
                day_number_row += '|' + day_number_label + " WORKER'S DAY" + (' ' * 2)
            elif current_date.month == 5 and current_date.day == 27:
                day_number_row += '|' + day_number_label + " CHILDREN'S DAY"
            elif current_date.month == 3 and current_date.day == 8:
                day_number_row += '|' + day_number_label + " WOMEN'S DAY" + (' ' * 3)
            elif current_date.month == 6 and current_date.day == 12:
                day_number_row += '|' + day_number_label + ' DEMOCRACY DAY' + (' ' * 1)
            else:
                day_number_row += '|' + day_number_label + (' ' * 15)
            
            current_date += datetime.timedelta(days=1)            
        day_number_row += '|\n'

        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        if current_date.month != month:
            break

    cal_text += week_seperator
    return cal_text


cal_text = get_calendar(year, month)
print(cal_text)

calendar_filename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendar_filename, 'w') as file_obj:
    file_obj.write(cal_text)

print('Saved to ' + calendar_filename)