# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

### Imports
from get_arguments import get_arguments
from buy import buy
from sell import sell
from advance import advance_time
from export import export, mark
from reset import reset
from report import reports
import file_tree
import time_data


# Your code below this line.

def main(args):
    ### Create databases
    file_tree.create_storage()
    time_data.get_current_date()

    ### Get arguments
    args = get_arguments()
    if args.action == 'buy':
        buy(args)
    elif args.action == 'sell':
        sell(args)
    elif args.action == 'time':
        advance_time(args)
    elif args.action == 'report':
        mark(args)
        reports(args)
    elif args.action == 'export':
        export(args)
    elif args.action == 'reset':
        reset()


if __name__ == "__main__":
    args = get_arguments()
    main(args)