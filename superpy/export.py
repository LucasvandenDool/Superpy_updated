import pandas as pd
import matplotlib.pyplot as plt
import os

### Gives a 'mark' so the program knows what the last report action was. 
### This is used to add the correct column names to the pdf export
def mark(args):
    if os.path.exists('databases\c_mark.txt'):
        os.remove('databases\c_mark.txt')
    
    new_mark = open('databases\c_mark.txt', 'a')

    if args.report_action == 'storage':
        marker = 'storage'
    
    if args.report_action == 'revenue':
        marker = 'revenue'

    if args.report_action == 'sales':
        marker = 'sales'

    if args.report_action == 'purchases':
        marker = 'purchases'
    
    if args.report_action == 'expiration':
        marker = 'expiration'
    
    new_mark.write(marker)
    new_mark.close()
    return
    
### Creates table and saves as PDF
def export_pdf(df):
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    plt.savefig('xport.pdf')
    return

### Main export function, reads the 'mark' to match correct column names.
def export(args):

    if args.export_action == 'storage':
        df = pd.read_csv('databases\storage.csv', header=None)
        df.columns = ['Product', 'Price', 'Amount', 'Purchase date', 'Expiration date']
        export_pdf(df)
       
    if args.export_action == 'report':
        with open('databases\c_mark.txt', 'r') as marker:
            action = marker.read()
            
            if action == 'storage':
                df = pd.read_csv('databases\\report.csv', header=None)
                df.columns = ['Product', 'Price', 'Amount', 'Purchase date', 'Expiration date']
                export_pdf(df)
            
            if action == 'revenue':
                df = pd.read_csv('databases\\report.csv', header=None)
                df.columns = ['Product', 'Buy Price', 'Sales Price', 'Amount', 'Sales date', 'Revenue']
                export_pdf(df)
            
            if action == 'sales':
                df = pd.read_csv('databases\\report.csv', header=None)
                df.columns = ['Product', 'Buy Price', 'Sell Price', 'Amount', 'Purchase date', 'Sell Date', 'Expiration date', 'Revenue', 'Profit']
                export_pdf(df)
            
            if action == 'purchases':
                df = pd.read_csv('databases\\report.csv', header=None)
                df.columns = ['Product', 'Buy Price', 'Amount', 'Purchase date', 'Expiration date']
                export_pdf(df)
            
            if action == 'expiration':
                df = pd.read_csv('databases\\report.csv', header=None)
                df.columns = ['Product', 'Buy Price', 'Amount', 'Purchase date', 'Expiration date', 'Loss']
                export_pdf(df)