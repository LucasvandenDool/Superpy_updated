Report:
When I started this assignment, I almost immediately panicked. When is was going through the assignment information, there were a lot of concepts I didn't know about. I had never worked with
argparse, datetime or csv files so it took a long time to get started, but eventually I got there. In total this assignment took me more than 4 weeks to complete.

I have got a lot of real life experience with WMS's, or wharehouse management systems. This meant I was familiar with all the functions I had to implement into the tool. This also meant I probally
made it harder for myself, but I wanted the tool to work properly. Some examples:

    - When you want to sell a product, you have to give a expiration date and purchase price. This was not stated in the original assignment, but from real life experience I knew this was necessary
        because you want to have control over which product you sell. When a product is going to expire whitin a few days, you want to sell this product instead of the product with a longer 
        expiration date. The same goes for the purchase price. When there is a low offer on a product, you want to sell the product you paid the least for. This way you can maximize the profit. 

    - Another feature I took from real life experience, is the scheduling of future purchases. This way you can enter a purchase into the system, the moment you made the purchase. It will however
        not show up in the storage report untill the product is actually in the supermarket. When advancing the date, you will see that the future purchases wil be added to the storage.
    
    - To generate the reports, I chose the pandas module. This module gives a very nice overview of the different csv-files. I tried to use pandas for all the data entries, but found it quite   
        difficult. So I only used pandas for the report function, where the results are the most visible.
    
    - I also had a lot of problems with the datetime module. I found it especially hard to 'date' my program, but at some point it just 'clicked'. I stored the internal date in a txt-file and from 
        then on I had a lot less problems.

In the end I'm quite satisfied with the product, although there's always room for improvement. I learned a lot making this tool!

#### NEW!
Changes made since last feedback:
- Fixed the 'no columns to parse' error when generating a report from a 'empty' list. This problem was adressed in the feedback video. 
- Added the use of the tabulate module to style the report output.
- Through the use of matplotlib and pandas there is now a function to export to PDF.
- The date can now be set to a desired date, instead of only advancing for a number of days.

