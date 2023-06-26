### Imports
from datetime import datetime, timedelta
import time_data
import os
import csv
import file_tree

### Advance time, set new date, update current_date.txt
def advance_time(args):

    ### Advancing time
    if args.advance_action == 'advance':
        today = time_data.get_current_date()
        advance = timedelta(days= args.amount)
        new_date = today + advance
        new_date = datetime.strftime(new_date, '%Y-%m-%d')
        os.remove('databases\current_date.txt')
        new_dates = open('databases\current_date.txt', 'a')
        new_dates.write(new_date)
        new_dates.close()
        return check_storage()
    
    ### Setting new date
    if args.advance_action == 'set':
        args.set = datetime.strptime(args.set, '%Y-%m-%d').date()

        if args.set == time_data.get_current_date():
            raise ValueError('Date to set is current date already.')
        
        if args.set < time_data.get_current_date():
            raise ValueError('Can not set date to past date.')
        
        if args.set > time_data.get_current_date():
            os.remove('databases\current_date.txt')
            new_date = str(args.set)
            new_dates = open('databases\current_date.txt', 'a')
            new_dates.write(new_date)
            new_dates.close()
            return check_storage()

### After advancing time => checks expiration dates and exports expired products
def check_storage():
    with open('databases\storage.csv', 'r') as storage, open('databases\\new_storage.csv', 'a', newline='') as new_storage, open(
        'databases\expired_products.csv', 'a', newline='') as expired_storage:
        reader = csv.reader(storage)
        writer = csv.writer(new_storage)
        exp_writer = csv.writer(expired_storage)

        for item in reader:
            item[4] = datetime.strptime(item[4], '%Y-%m-%d').date()
            
            if item[4] < time_data.get_current_date():
                loss = float(item[1]) * int(item[2])
                new_item = [item[0], item[1], item[2], item[3], item[4], loss]
                exp_writer.writerow(new_item)
            
            else:
                writer.writerow(item)
                
### After advancing time => checks future purchases and exports to storage
    with open('databases\\future_storage.csv', 'r') as future_storage, open('databases\\new_future_storage.csv', 'a', newline='') as new_future_storage, open(
        'databases\\new_storage.csv', 'a', newline='') as new_storage, open('databases\purchase_storage.csv', 'a', newline='') as purchase_storage:
        future_reader = csv.reader(future_storage)
        future_writer = csv.writer(new_future_storage)
        writer = csv.writer(new_storage)
        purchase_writer = csv.writer(purchase_storage)
        

        for product in future_reader:
            product[3] = datetime.strptime(product[3], '%Y-%m-%d').date()
            
            if product[3] <= time_data.get_current_date():
                writer.writerow(product)
                purchase_writer.writerow(product)

            else:
                future_writer.writerow(product)
    
    file_tree.wipe_and_rename()
    file_tree.future_wipe_and_rename()
    print(f'The current date is: {time_data.get_current_date()}')