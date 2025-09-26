"""This is calculator cli

calc.py <operation> <arg1> <arg2>

# Examples

calc.py add 1 2
calc.py sub 5 4
calc.py mul 5 4
calc.py div 5 4
calc.py mod 5 4
"""

import sys

supported_ops = ["add", "sub", "mul", "div", "mod"]


def cli_help():
    """Generates the help
    """
    print("Calculator cli usage")
    print("calc.py <operation> <arg1> <arg2>")
    print("""
            calc.py add 1 2
            calc.py sub 5 4
            calc.py mul 5 4
            calc.py div 5 4
            calc.py mod 5 4
          """)

def validate_args(args:list[str]):
    """This function validates the arguments

    Args:
        args (_type_): _description_
    """
    if len(args) != 3:
        cli_help()
        print("Invalid arguments")
        exit(1)
    if args[0].lower() not in supported_ops:
        cli_help()
        print(f"unsupported operation. supported operations are {','.join(supported_ops)}")
        exit(2)
    if not (args[1].isdigit() and args[2].isdigit()):
        cli_help()
        print("This operation expects numbers as arguments")
        exit(3)

def calcualte(args:list[str]):
    """This performs calculations

    Args:
        args (list[str]): _description_
    """
    value1 = int(args[1])
    value2 = int(args[2])
    if args[0].lower() == 'add':
        print(value1 + value2)
    if args[0].lower() == 'sub':
        print(value1 - value2)
    if args[0].lower() == 'mul':
        print(value1 * value2)
    if args[0].lower() == 'div':
        print(value1 / value2)
    if args[0].lower() == 'mod':
        print(value1 % value2)
    exit(0)

def main():
    """Entry point for cli application
    """
    args = sys.argv[1::]
    validate_args(args)
    calcualte(args)


if __name__ == "__main__":
    main()
