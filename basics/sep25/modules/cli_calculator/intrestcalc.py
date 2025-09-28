"""This is simple intrest calculator cli

intrestcalc.py --principal 10000 --time 3 --rate 24
intrestcalc.py -p 10000 -t 3 -r 24


"""

import argparse

def simple_intrest(prinicpal: float, rate: int, time: int) -> float:
    """Simple intrest calculator

    Args:
        prinicpal (float): _description_
        rate (int): _description_
        time (int): _description_

    Returns:
        float: simple intrest
    """
    return prinicpal * time * rate / 100


def main():
    """Entry point
    """
    parser = argparse.ArgumentParser(
        description="simple intrest caclulator",
        epilog="This is simple intrest calcualtor"
    )
    parser.add_argument('-p', '--principal', type=float)
    parser.add_argument('-t', '--time', type=int)
    parser.add_argument('-r', '--rate', type=int)
    args = parser.parse_args()
    print(simple_intrest(args.principal, args.rate, args.time))

if __name__ == '__main__':
    main()
