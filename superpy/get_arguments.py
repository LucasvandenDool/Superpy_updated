### Imports
import argparse 


def get_arguments():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='action')

    # Buy product
    buy_prs = subparser.add_parser('buy', help='Buy product')
    buy_prs.add_argument('-n', '--name', type=str.capitalize, help='Name of product you want to buy.')
    buy_prs.add_argument('-p', '--price', type=float, help='Price of product you want to buy. Requires float.')
    buy_prs.add_argument('-a', '--amount', type=int, help='Amount of products you want to buy. Requires integer.')
    buy_prs.add_argument('-d', '--date', type=str, help='Date of purchase, formatted: YYYY-MM-DD. Give future date to schedule purchase.')
    buy_prs.add_argument('-e', '--expiration', type=str, help='Expiration date of product you want to buy, formatted: YYYY-MM-DD')

    # Sell Product
    sell_prs = subparser.add_parser('sell', help='Sell product')
    sell_prs.add_argument('-n', '--name', type=str.capitalize, help='Name of product you want to sell.')
    sell_prs.add_argument('-p', '--price', type=float, help='Sales price of the product you want to sell. Requires float.')
    sell_prs.add_argument('-a', '--amount', type=int, help='Amount of products you want to sell. Requires integer.')
    sell_prs.add_argument('-e', '--expiration', type=str, help='Expiration date of product you want to sell, formatted: YYYY-MM-DD')
    sell_prs.add_argument('-pp', '--purchase_price', type=float, help='Purchase price of the product you want to sell. Requires float.')
    
    # Advance time
    advance_prs = subparser.add_parser('time', help='Set date or advance time')
    advance_prs.add_argument('advance_action', choices=['set', 'advance'], help='Choose between setting the date or advancing time')
    advance_prs.add_argument('-s', '--set', type=str, help= 'Set date to future date, formatted: YYYY-MM-DD')
    advance_prs.add_argument('-a', '--amount', type=int, help= 'Advance time by number of days.')


    # Report
    report_parser = subparser.add_parser('report', help='Generate a report')
    report_parser.add_argument('report_action', choices=['storage', 'revenue', 'profit', 'sales', 'purchases', 'expiration'], help='Choose between report actions')
    report_parser.add_argument('-d', '--date', type=str, help='Date to generate report on, formatted: YYYY-MM-DD')
    report_parser.add_argument('-ed', '--end_date', type=str, help='Optional. Add enddate to generate report over multiple days, "--date" will be used as startdate. Not used for the "storage" action. Formatted: YYYY-MM-DD')
    
    # Export
    export_parser = subparser.add_parser('export', help='Export to PDF')
    export_parser.add_argument('export_action', choices=['storage', 'report'], help='Choose between exporting actions. "storage" for the current storage, "report" for the latest report.')
    
    # Reset databases
    advance_prs = subparser.add_parser('reset', help='WARNING! Clears all databases')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    pass