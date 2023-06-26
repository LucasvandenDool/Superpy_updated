This python tool is made as a storage managment system for supermarkets. With this tool you can:

    - Buy Products, also possible to schedule future purchases
    - Sell Products
    - Keep track of expired products.
    - Generate a storage overview for the current date or a date in the past.
    - Setting the date to a future date.
    - Advance time to keep the tool up to date.
    - Generate a revenue overview, for a single date or a longer period.
    - Generate a profit overview, for a single date or a longer period.
    - Generate a sales overview,  for a single date or a longer period.
    - Generate a purchase overview, for a single date or a longer period.
    - Export storage or report to PDF.
    - Reset all the databases, including the date.
    - Use the -h, -help command to advance through all the different options.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to start:
    The first step in using the tool is opening the tool in powershell, then you are ready to buy your first product.
        python superpy.py -h    \\ This will bring up the help menu and all the option for the tool. There are 5 arguments to choose from here:

        buy                 Buy product
        sell                Sell product
        advance             Advance time
        report              Generate a report
        reset               WARNING! Clears all databases
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    When you choose to buy a product, you can use the -h command again to see all the requirements for a succesfull purchase:
        python superpy.py buy -h    \\ This will bring up all the requirements.

        -n NAME, --name NAME  Name of product you want to buy.
        -p PRICE, --price PRICE  Price of product you want to buy. Requires float.
        -a AMOUNT, --amount AMOUNT  Amount of products you want to buy. Requires integer.
        -d DATE, --date DATE  Date of purchase, formatted: YYYY-MM-DD. Give future date to schedule purchase.
        -e EXPIRATION, --expiration EXPIRATION  Expiration date of product you want to buy, formatted: YYYY-MM-DD
    
    Examples:
    - python superpy.py buy -n cheese -p 3.25 -a 25 -d 2023-06-01 -e 2023-08-01
    - python superpy.py buy -n beer -p 1.15 -a 100 -d 2023-06-25 -e 2023-07-18
    - python superpy.py buy -n toothpaste -p 8.90 -a 22 -2023-05-31 -e 2024-01-01
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    When you choose to sell a product, you can use the -h command again to see all the requirements for a succesfull sale:
        python superpy.py sell -h

        -n NAME, --name NAME  Name of product you want to sell.
        -p PRICE, --price PRICE  Sales price of the product you want to sell. Requires float.
        -a AMOUNT, --amount AMOUNT  Amount of products you want to sell. Requires integer.
        -e EXPIRATION, --expiration EXPIRATION  Expiration date of product you want to sell, formatted: YYYY-MM-DD
        -pp PURCHASE_PRICE, --purchase_price PURCHASE_PRICE  Purchase price of the product you want to sell. Requires float.
    
    Examples:
    - python superpy.py sell -n cheese -p 5.50 -a 10 -e 2023-08-01 -pp 3.25
    - python superpy.py sell -n beer -p 3.49 -a 25 -e 2023-07-18 -pp 1.15
    - python superpy.py sell -n toothpaste -p 12.30 -a 6 -e 2024-01-01 -pp 8.90
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##### NEW!    
    When you want to alter the internal date of the tool, you can use the -h command to see all the requirements for advancing the date:
        python superpy.py time -h

        set                 Set the internal date to a desired future date.
        advance             Advance the internal date by a desired number of days.

        -s SET, --set SET   Set date to future date, formatted: YYYY-MM-DD
        -a AMOUNT, --amount AMOUNT  Advance time by number of days.

    Example:
    - python superpy.py time set -s 2024-01-01
    - python superpy.py time advance -a 1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    When you want to generate a report, you can use the -h command to see all the different report options you can generate:
        python superpy.py report -h

        storage             Generate a storage overview
        revenue             Generate a revenue overview
        profit              Generate a profit overview
        sales               Generate a sales overview
        purchases           Generate a purchase overview
        expiration          Generate a expired products overview
    
        -d DATE, --date DATE  Date to generate report on, formatted: YYYY-MM-DD
        -ed END_DATE, --end_date END_DATE  Optional. Add enddate to generate report over multiple days, "--date" will be used as startdate. Not used for the "storage" action. Formatted: YYYY-MM-DD
    
    All the report options require at least a single date, and an end date when you want to generate a report over multiple dates. The storage report is the only one where the end date option will NOT work.

    Examples:
    - python superpy.py report storage -d 2023-06-01
    - python superpy.py report revenue -d 2023-07-05
    - python superpy.py report revenue -d 2023-07-05 -ed 2024-05-07
    - python superpy.py report profit -d 2023-05-31
    - python superpy.py report profit -d 2023-05-31 -ed 2023-06-01
    - python superpy.py report sales -d 2023-06-12
    - python superpy.py report sales -d 2023-06-12 -ed 2023-06-18
    - python superpy.py report purchases -d 2023-05-31
    - python superpy.py report purchases -d 2023-05-31 -ed 2023-08-01
    - python superpy.py report expiration -d 2023-08-12
    - python superpy.py report expiration -d 2023-06-02 -ed 2023-06-03
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### NEW!    
    When you want to export to PDF, you can use the -h command to see all the different report options:
        python superpy.py export -h

        storage         Export current storage to PDF
        report          Export latest report to PDF

    Examples:
    - python superpy.py export storage
    - python superpy.py export report
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    When you want to reset the databases, you can use this command:
        python superpy.py reset  WARNING! Clears all databases
    
