"""This is calculator cli

calc.py <operation> <arg1> <arg2>

# Examples

calc.py add 1 2
calc.py sub 5 4
calc.py mul 5 4
calc.py div 5 4
calc.py mod 5 4
"""

import argparse
supported_ops = ["add", "sub", "mul", "div", "mod"]


def main():
    """Entry point
    """
    parser = argparse.ArgumentParser("calc", description="Calculator")
    parser.add_argument("operation", choices=supported_ops)
    parser.add_argument("value1", type=int)
    parser.add_argument("value2", type=int)
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()
