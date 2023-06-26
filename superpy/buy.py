### Imports
import csv
import file_tree
from time_data import get_current_date
from datetime import datetime

### Buy product
def buy(args):
    args.date = datetime.strptime(args.date, '%Y-%m-%d').date()
    args.expiration = datetime.strptime(args.expiration, '%Y-%m-%d').date()
    
    ### Check date for validity
    if args.date < get_current_date():
        
        raise ValueError('Can only make a purchase today or on future date')
    
    if args.expiration < get_current_date():
        raise ValueError('Expiration date can only be future date.')

    
    ### Adding purchase to purchase register
    with open('databases\purchase_storage.csv', 'a', newline='') as purchase_storage:
        if args.date == get_current_date():
            purchase_writer = csv.writer(purchase_storage)
            purchase_log = [args.name, args.price, args.amount, args.date, args.expiration]
            purchase_writer.writerow(purchase_log)
    
    
    ### Placing product in storage
    with open('databases\storage.csv', 'r') as store, open('databases\\new_storage.csv', 'a', newline='') as new_storage, open(
        'databases\\new_future_storage.csv', 'a', newline='') as future_storage_app, open('databases\\future_storage.csv', 'r') as future_storage_read:
        
        reader = csv.reader(store)
        writer = csv.writer(new_storage)
        
        future_reader = csv.reader(future_storage_read)
        future_writer = csv.writer(future_storage_app)

        in_storage = False   
        future_storage_wipe = False


        ### Already in storage with same expiration date    
        for item in reader:
            item[4] = datetime.strptime(item[4], '%Y-%m-%d').date()
            
            if args.name == item[0] and args.price == float(item[1]) and args.expiration == item[4] and args.date == get_current_date():
                new_amount = int(item[2]) + int(args.amount)
                item[2] = new_amount
                writer.writerow(item)
                in_storage = True
                
            else:
                writer.writerow(item)
                

        ### New Product
        if not in_storage:
            
            if args.date == get_current_date():
                new_product = [args.name, args.price, args.amount, args.date, args.expiration]
                writer.writerow(new_product)
                in_storage = True

            ### Future purchase    
            else:
                for fut_item in future_reader:
                    fut_item[4] = datetime.strptime(fut_item[4], '%Y-%m-%d').date()
                    fut_item[3] = datetime.strptime(fut_item[3], '%Y-%m-%d').date()
                    
                    if args.name == fut_item[0] and args.price == float(fut_item[1]) and args.expiration == fut_item[4] and args.date == fut_item[3]:
                        fut_new_amount = int(fut_item[2]) + int(args.amount)
                        fut_item[2] = fut_new_amount
                        future_writer.writerow(fut_item)
                        in_storage = True
                        future_storage_wipe = True

                    else:
                        future_writer.writerow(fut_item)
                        future_storage_wipe = True
            
        if not in_storage:
            fut_new_product = [args.name, args.price, args.amount, args.date, args.expiration]
            future_writer.writerow(fut_new_product)
            future_storage_wipe = True

    ### Updating storage
    file_tree.wipe_and_rename()
    if future_storage_wipe:
        file_tree.future_wipe_and_rename()
    else:
        file_tree.future_remove()
    
    

if __name__ == "__main__":
    pass