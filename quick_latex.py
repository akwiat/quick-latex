import argparse

parser = argparse.ArgumentParser(description='quick-compile a problem')
parser.add_argument('filename', type=str, help='name of the .tex file to compile')
# parser.add_argument('worksheet_name', nargs='?', type=str, help='name of the worksheet')
# parser.add_argument('--all', action='store_true', help='update all worksheets')

if __name__ == "__main__":
    args = parser.parse_args()
    print("filename: {}".format(args.filename))
