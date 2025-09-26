import sys
import calc

if __name__ == '__main__':
    args = sys.argv[1::]
    print(args)
    if len(args) != 3:
        print("Not enough arguments passed")
    if args[0] == 'add':
        print(calc.add(int(args[1]), int(args[2])))

    
