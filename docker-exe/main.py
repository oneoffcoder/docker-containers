import json
import argparse
import sys

def parse_args(args):
    """
    Parses arguments.
    :return: Arguments.
    """
    parser = argparse.ArgumentParser('Hello World')

    parser.add_argument('-f', '--first_name', help='first name', required=True)
    parser.add_argument('-m', '--middle_name', help='middle name', required=False)
    parser.add_argument('-l', '--last_name', help='last name', required=True)
    parser.add_argument('--version', action='version', version='%(prog)s v0.0.1')

    return parser.parse_args(args)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print('arguments')
    print(json.dumps(vars(args), indent=1, sort_keys=True))

    full_name = [args.first_name, args.middle_name, args.last_name]
    full_name = filter(lambda n: n is not None and len(n.strip()) > 0, full_name)
    full_name = ' '.join(full_name)
    print('hello, {}!'.format(full_name))
