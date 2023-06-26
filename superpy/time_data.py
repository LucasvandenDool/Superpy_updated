### Imports
import datetime
import os


### Establish today at first try, and store present date
def get_current_date():
    if os.path.exists('databases\current_date.txt'):
        with open('databases\current_date.txt', 'r') as dates:
            content = dates.read()
            content = datetime.datetime.strptime(content, '%Y-%m-%d').date()
            return content
    
    else:
        new_dates = open('databases\current_date.txt', 'a')
        today = datetime.date.today()
        today = today.strftime('%Y-%m-%d')
        new_dates.write(today)
        new_dates.close()
        return get_current_date()


if __name__ == "__main__":
    pass