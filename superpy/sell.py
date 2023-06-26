### Imports
import csv
import os
import time_data
import file_tree

### Sell product
def sell(args):
    with open('databases\storage.csv', 'r') as store, open('databases\\new_sell_storage.csv', 'a', newline='') as new_storage, open('databases\sales_storage.csv', 'a', newline='') as sales_storage:
        reader = csv.reader(store)
        writer = csv.writer(new_storage)
        sales_writer = csv.writer(sales_storage)
        

        ### Check voor name and expiration
        for item in reader:

            if args.name == item[0] and args.purchase_price == float(item[1]) and args.expiration == item[4]:
                new_amount = int(item[2]) - int(args.amount)
                if new_amount == 0:
                    print('Product is now sold out')
                    revenue = round(float(args.price) * int(args.amount), 2)
                    profit = round((float(args.price) * int(args.amount)) - (float(item[1]) * int(args.amount)), 2)
                    sell_date = time_data.get_current_date()
                    new_sale = [args.name, item[1], args.price, args.amount, item[3], sell_date, args.expiration, revenue, profit]
                    sales_writer.writerow(new_sale)    
                    

                elif new_amount <= 0:
                    raise ValueError('Not enough stock.')

                else:
                    item[2] = new_amount
                    writer.writerow(item)
                    revenue = round(float(args.price) * int(args.amount), 3)
                    profit = round((float(args.price) * int(args.amount)) - (float(item[1]) * int(args.amount)), 3)
                    sell_date = time_data.get_current_date()
                    new_sale = [args.name, item[1], args.price, args.amount, item[3], sell_date, args.expiration, revenue, profit]
                    sales_writer.writerow(new_sale)
            
            else:
                writer.writerow(item)
                
    ### Updating storage file
    file_tree.sales_wipe_and_rename()


if __name__ == "__main__":
    pass