"""Advanced calculator

advcalc.py basic --op add 10 20 
advcalc.py basic --op sub 10 20
advcalc.py intrest --type simple --principal 10000 --time 3 --rate 24
"""
import argparse


def main():
    """Main function
    """
    parser = argparse.ArgumentParser("advcalc", description="advanced calculator")
    sub_parser = parser.add_subparsers(help='sub command help',dest='command')
    basic = sub_parser.add_parser('basic')
    basic.add_argument("-o", "--op", type=str, choices=['add', 'sub'],help="operation")
    basic.add_argument('values', nargs="*",  help='numeric values')

    intrest_parser = sub_parser.add_parser('intrest')
    intrest_parser.add_argument('--type', type=str, choices=['si', 'ci'], help='type of intrest')
    intrest_parser.add_argument('-p', '--principal', type=float, default=10000, help="principal amount")
    intrest_parser.add_argument('-t', '--time', type=int, default=3, help="time in years")
    intrest_parser.add_argument('-r', '--rate', type=int, default=24, help="annual rate of intrest")
    args = parser.parse_args()
    print(args)
    if args.command == "basic":
        # perform operations
        pass
    elif args.command == "intrest":
        # perform intrest
        pass







if __name__ == '__main__':
    main()