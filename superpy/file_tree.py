### Imports
import os


def create_storage():
    if not os.path.exists('databases'):
        os.makedirs('databases')
        
    if not os.path.exists('databases\storage.csv'):
        with open('databases\storage.csv', 'w'):
            
                if not os.path.exists('databases\\future_storage.csv'):
                    with open('databases\\future_storage.csv', 'w'):
                    
                        if not os.path.exists('databases\sales_storage.csv'):
                            with open('databases\sales_storage.csv', 'w'):
                            
                                if not os.path.exists('databases\expired_products.csv'):
                                    with open('databases\expired_products.csv', 'w'):
                                        
                                        if not os.path.exists('databases\purchase_storage.csv'):
                                            with open('databases\purchase_storage.csv', 'w'):

                                                if not os.path.exists('databases\c_mark.txt'):
                                                    with open('databases\c_mark.txt', 'w'):
                                                        return
            
### Updating storage file
def wipe_and_rename():
    os.remove('databases\storage.csv')
    os.rename('databases\\new_storage.csv', 'databases\storage.csv')

def future_wipe_and_rename():
    os.remove('databases\\future_storage.csv')
    os.rename('databases\\new_future_storage.csv', 'databases\\future_storage.csv')

def sales_wipe_and_rename():
    os.remove('databases\storage.csv')
    os.rename('databases\\new_sell_storage.csv', 'databases\storage.csv')

def future_remove():
    os.remove('databases\\new_future_storage.csv')

def storage_remove():
    os.remove('databases\\new_storage.csv')
