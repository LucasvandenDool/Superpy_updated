### Imports
import shutil
import file_tree
import time_data

def reset():
    shutil.rmtree('databases')
    file_tree.create_storage()
    time_data.get_current_date()