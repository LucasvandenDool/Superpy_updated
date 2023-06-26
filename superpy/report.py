### Imports
import pandas as pd
from time_data import get_current_date
import tabulate as tb
import os
import csv
from datetime import datetime

### Generate past storage \ Called upon by reports function
def past_storage(date):
    with open('databases\storage.csv', 'r') as storage, open('databases\sales_storage.csv', 'r') as sales, open(
        'databases\expired_products.csv', 'r') as expired, open('databases\\report.csv', 'a', newline='') as report:
        storage_reader = csv.reader(storage)
        sales_reader = csv.reader(sales)
        expired_reader = csv.reader(expired)
        writer = csv.writer(report)
        
        ### Looping through current storage to rebuild report storage
        for item in storage_reader:            
            item[3] = datetime.strptime(item[3], '%Y-%m-%d').date()
            if item[3] <= date:
                writer.writerow(item)

        ### Looping through expired products to rebuild report storage
        for exp in expired_reader:
            exp[3] = datetime.strptime(exp[3], '%Y-%m-%d').date()
            exp[4] = datetime.strptime(exp[4], '%Y-%m-%d').date()
            if exp[4] >= date and exp[3] <= date:
                new_exp = [exp[0], exp[1], exp[2], exp[3], exp[4]]
                writer.writerow(new_exp)
    
        ### Looping through sold products to rebuild report storage    
        for sale in sales_reader:
            sale[5] = datetime.strptime(sale[5], '%Y-%m-%d').date()
            if sale[5] >= date:                
                if str(sale[0]) == str(item[0]) and float(sale[1]) == float(item[1]) and int(sale[6]) == int(item[4]):
                    new_amount = int(item[4]) + int(sale[6])
                    item[4] = new_amount 

                new_sale = [sale[0], sale[1], sale[3], sale[4], sale[6]]
                writer.writerow(new_sale)


### Generate reports
def reports(args):
    
    ### Converting dates
    args.date = datetime.strptime(args.date, '%Y-%m-%d').date()
    if args.end_date:
        args.end_date = datetime.strptime(args.end_date, '%Y-%m-%d').date()
        ### Checking enddate for validity
        if args.end_date < args.date:
            raise ValueError('End date must be later than the start date.')

    ### Clear previous report
    if os.path.exists('databases\\report.csv'):
        os.remove('databases\\report.csv')
       

### INVENTORY REPORT
    if args.report_action == 'storage':
        with open('databases\storage.csv', 'r') as storage, open('databases\\report.csv', 'a', newline='') as report:
            reader = csv.reader(storage)
            writer = csv.writer(report)
            
            if args.date == get_current_date():
                for item in reader:
                    writer.writerow(item)

            elif args.date < get_current_date():
                past_storage(args.date)

            elif args.date > get_current_date():
                raise ValueError('Can not generate storage report of future date, try advancing time.')           

        ### Checking if report is empty
        if os.path.getsize('databases\\report.csv') == 0:
            raise ValueError('Storage is/was empty on that date.')
        
        ### Building dataframe
        storage_data = pd.read_csv('databases\\report.csv', header=None)
        columns= ['Product', 'Price', 'Amount', 'Purchase date', 'Expiration date']
        data_frame = pd.DataFrame(storage_data)
        data_frame.columns = columns
        print(tb.tabulate(data_frame, headers= columns, tablefmt="rounded_grid"))


### REVENUE REPORT
    if args.report_action == 'revenue':
        with open('databases\sales_storage.csv', 'r') as sales, open('databases\\report.csv', 'a', newline='') as report:
            reader = csv.reader(sales)
            writer = csv.writer(report)
            
            if not args.end_date:
                for item in reader:
                    item[5] = datetime.strptime(item[5], '%Y-%m-%d').date()
                    
                    if args.date == item[5]:
                        revenue_report_item = (item[0], item[1], item[2], item[3], item[5], item[7])
                        writer.writerow(revenue_report_item)
            
            else:
                for item in reader:
                    item[5] = datetime.strptime(item[5], '%Y-%m-%d').date()

                    if item[5] >= args.date and item[5] <= args.end_date:
                        revenue_report_item = (item[0], item[1], item[2], item[3], item[5], item[7])
                        writer.writerow(revenue_report_item)
        
        ### Checking if report is empty
        if os.path.getsize('databases\\report.csv') == 0:
            raise ValueError('No revenue to report during that period.')
        
        ### Building dataframe
        revenue_data = pd.read_csv('databases\\report.csv', header=None)
        columns= ['Product', 'Buy Price', 'Sales Price', 'Amount', 'Sales date', 'Revenue']
        data_frame = pd.DataFrame(revenue_data)
        data_frame.columns = columns
        data_frame.loc['Total Revenue'] = pd.Series(data_frame['Revenue'].sum(), index=['Revenue'])
        print(tb.tabulate(data_frame, headers= columns, tablefmt="rounded_grid"))


### PROFIT REPORT
    if args.report_action == 'profit':
        no_sales = True
        no_exp = True

        ### Profit for a SINGLE DATE
        if not args.end_date:
            with open('databases\sales_storage.csv', 'r') as sales, open('databases\\report.csv', 'a', newline='') as report:
                sales_reader = csv.reader(sales)
                writer = csv.writer(report)
        
                for sale in sales_reader:
                    sale[5] = datetime.strptime(sale[5], '%Y-%m-%d').date()
                    
                    if args.date == sale[5]:
                        profit_report_sale = (sale[0], sale[1], sale[2], sale[3], sale[5], sale[8])
                        writer.writerow(profit_report_sale)
                        no_sales = False

            ### Building dataframe for salesprofit and clearing report
            if no_sales == False:
                profit_data = pd.read_csv('databases\\report.csv', header=None)
                columns= ['Product', 'Buy Price', 'Sales Price', 'Amount', 'Sales date', 'Profit']
                data_frame = pd.DataFrame(profit_data)
                data_frame.columns = columns
                data_frame.loc['Total Profit Sales'] = pd.Series(data_frame['Profit'].sum(), index=['Profit'])
                print(tb.tabulate(data_frame, headers=columns, tablefmt="rounded_grid"))            
                os.remove('databases\\report.csv')

            with open('databases\expired_products.csv', 'r') as expired, open('databases\\report.csv', 'a', newline='') as report:
                expired_reader = csv.reader(expired)
                writer = csv.writer(report)
                
                for expired in expired_reader:
                    expired[4] = datetime.strptime(expired[4], '%Y-%m-%d').date()
                    
                    if args.date == expired[4]:
                        profit_report_expired = (expired[0], expired[1], expired[2], expired[4], expired[5])
                        writer.writerow(profit_report_expired)
                        no_exp = False

            ### Building dataframe for expiration loss
            if no_exp == False:
                profit_data_exp = pd.read_csv('databases\\report.csv', header=None)
                columns_exp= ['Product', 'Buy Price', 'Amount', 'Expiration date', 'Loss']
                data_frame_exp = pd.DataFrame(profit_data_exp)
                data_frame_exp.columns = columns_exp
                data_frame_exp.loc['Total Expiration Loss'] = pd.Series(data_frame_exp['Loss'].sum(), index=['Loss'])
                print(tb.tabulate(data_frame_exp, headers= columns_exp, tablefmt="rounded_grid"))        
            
            ### Calculating total profit
            if no_sales == False and no_exp == False:
                total_profit = ((data_frame.loc['Total Profit Sales'][-1]) - (data_frame_exp.loc['Total Expiration Loss'][-1]))
                print(f'Total profit is {total_profit}')
            
            if no_sales == False and no_exp == True:
                total_profit = ((data_frame.loc['Total Profit Sales'][-1]) - 0)
                print(f'Total profit is {total_profit}')
            
            if no_sales == True and no_exp == False:
                total_profit = (0 - (data_frame_exp.loc['Total Expiration Loss'][-1]))
                print(f'Total profit is {total_profit}')

            if no_sales == True and no_exp == True:
                print('No profit to report.')

        ### Profit over a PERIOD
        else:
            with open('databases\sales_storage.csv', 'r') as sales, open('databases\\report.csv', 'a', newline='') as report:
                sales_reader = csv.reader(sales)
                writer = csv.writer(report)
        
                for sale in sales_reader:
                    sale[5] = datetime.strptime(sale[5], '%Y-%m-%d').date()

                    if sale[5] >= args.date and sale[5] <= args.end_date:
                        profit_report_sale = (sale[0], sale[1], sale[2], sale[3], sale[5], sale[8])
                        writer.writerow(profit_report_sale)
                        no_sales = False
            
            ### Building dataframe for salesprofit and clearing report
            if no_sales == False:
                profit_data = pd.read_csv('databases\\report.csv', header=None)
                columns= ['Product', 'Buy Price', 'Sales Price', 'Amount', 'Sales date', 'Profit']
                data_frame = pd.DataFrame(profit_data)
                data_frame.columns = columns
                data_frame.loc['Total Profit Sales'] = pd.Series(data_frame['Profit'].sum(), index=['Profit'])
                print(tb.tabulate(data_frame, headers= columns, tablefmt="rounded_grid"))            
                os.remove('databases\\report.csv')

            with open('databases\expired_products.csv', 'r') as expired, open('databases\\report.csv', 'a', newline='') as report:
                expired_reader = csv.reader(expired)
                writer = csv.writer(report)
                
                for expired in expired_reader:
                    expired[4] = datetime.strptime(expired[4], '%Y-%m-%d').date()

                    if expired[4] >= args.date and expired[4] <= args.end_date:
                        profit_report_expired = (expired[0], expired[1], expired[2], expired[4], expired[5])
                        writer.writerow(profit_report_expired)
                        no_exp = False
                    
            ### Building dataframe for expiration loss
            if no_exp == False:
                profit_data_exp = pd.read_csv('databases\\report.csv', header=None)
                columns_exp= ['Product', 'Buy Price', 'Amount', 'Expiration date', 'Loss']
                data_frame_exp = pd.DataFrame(profit_data_exp)
                data_frame_exp.columns = columns_exp
                data_frame_exp.loc['Total Expiration Loss'] = pd.Series(data_frame_exp['Loss'].sum(), index=['Loss'])
                print(tb.tabulate(data_frame_exp, headers= columns_exp, tablefmt="rounded_grid"))        

            ### Calculating total profit
            if no_sales == False and no_exp == False:
                total_profit = ((data_frame.loc['Total Profit Sales'][-1]) - (data_frame_exp.loc['Total Expiration Loss'][-1]))
                print(f'Total profit is {total_profit}')
            
            if no_sales == False and no_exp == True:
                total_profit = ((data_frame.loc['Total Profit Sales'][-1]) - 0)
                print(f'Total profit is {total_profit}')
            
            if no_sales == True and no_exp == False:
                total_profit = (0 - (data_frame_exp.loc['Total Expiration Loss'][-1]))
                print(f'Total profit is {total_profit}')

            if no_sales == True and no_exp == True:
                print('No profit to report.') 


### SALES REPORT
    if args.report_action == 'sales':
        with open('databases\sales_storage.csv', 'r') as sales, open('databases\\report.csv', 'a', newline='') as report:
            reader = csv.reader(sales)
            writer = csv.writer(report)

            ### Sales for a SINGLE DATE
            if not args.end_date:
                for item in reader:
                    item[5] = datetime.strptime(item[5], '%Y-%m-%d').date()

                    if args.date == item[5]:
                        writer.writerow(item)
            
            ### Sales for a PERIOD
            else:
                for item in reader:
                    item[5] = datetime.strptime(item[5], '%Y-%m-%d').date()

                    if item[5] >= args.date and item[5] <= args.end_date:
                        writer.writerow(item)

        ### Checking if report is empty
        if os.path.getsize('databases\\report.csv') == 0:
            raise ValueError('No sales on that date.')
        
        ### Building dataframe
        sales_data = pd.read_csv('databases\\report.csv', header=None)
        columns= ['Product', 'Buy Price', 'Sell Price', 'Amount', 'Purchase date', 'Sell Date', 'Expiration date', 'Revenue', 'Profit']
        data_frame = pd.DataFrame(sales_data)
        data_frame.columns = columns
        print(tb.tabulate(data_frame, headers= columns, tablefmt="rounded_grid"))

### PURCHASE REPORT
    if args.report_action == 'purchases':
        with open('databases\purchase_storage.csv', 'r') as purchase, open('databases\\report.csv', 'a', newline='') as report:
            reader = csv.reader(purchase)
            writer = csv.writer(report)

            ### Purchases for a SINGLE DATE
            if not args.end_date:
                for item in reader:
                    item[3] = datetime.strptime(item[3], '%Y-%m-%d').date()

                    if args.date == item[3]:
                        writer.writerow(item)
            
            ### Purchases for a PERIOD
            else:
                for item in reader:
                    item[3] = datetime.strptime(item[3], '%Y-%m-%d').date()

                    if item[3] >= args.date and item[3] <= args.end_date:
                        writer.writerow(item)

        ### Checking if report is empty
        if os.path.getsize('databases\\report.csv') == 0:
            raise ValueError('No purchases on that date.')
        
        ### Building dataframe
        purchase_data = pd.read_csv('databases\\report.csv', header=None)
        columns= ['Product', 'Buy Price', 'Amount', 'Purchase date', 'Expiration date']
        data_frame = pd.DataFrame(purchase_data)
        data_frame.columns = columns
        print(tb.tabulate(data_frame, headers= columns, tablefmt="rounded_grid"))


### EXPIRATION REPORT
    if args.report_action == 'expiration':
        with open('databases\expired_products.csv', 'r') as expired, open('databases\\report.csv', 'a', newline='') as report:
            reader = csv.reader(expired)
            writer = csv.writer(report)

            ### Expired products for a SINGLE DATE
            if not args.end_date:
                for item in reader:
                    item[4] = datetime.strptime(item[4], '%Y-%m-%d').date()

                    if args.date == item[4]:
                        writer.writerow(item)
            
            ### Expired products for a PERIOD
            else:
                for item in reader:
                    item[4] = datetime.strptime(item[4], '%Y-%m-%d').date()

                    if item[4] >= args.date and item[4] <= args.end_date:
                        writer.writerow(item)

        ### Checking if report is empty
        if os.path.getsize('databases\\report.csv') == 0:
            raise ValueError('No expired products on that date.')
        
        ### Building dataframe
        expired_data = pd.read_csv('databases\\report.csv', header=None)
        columns= ['Product', 'Buy Price', 'Amount', 'Purchase date', 'Expiration date', 'Loss']
        data_frame = pd.DataFrame(expired_data)
        data_frame.columns = columns
        print(tb.tabulate(data_frame, headers= columns, tablefmt="rounded_grid"))