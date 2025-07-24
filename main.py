import argparse



def get_parser_attrs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", metavar='N', nargs="+", required=True)

    return parser.parse_args()

args = get_parser_attrs()
print(args)


