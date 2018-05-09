import argparse
import os

from string import Template
from pkg_resources import resource_string

parser = argparse.ArgumentParser(description='quick-compile a problem')
parser.add_argument('filename', type=str, help='name of the .tex file to compile')
# parser.add_argument('worksheet_name', nargs='?', type=str, help='name of the worksheet')
# parser.add_argument('--all', action='store_true', help='update all worksheets')

def ensure_dir(d):
    try:
        os.mkdir(d)
    except:
        pass

if __name__ == "__main__":
    args = parser.parse_args()
    print("filename: {}".format(args.filename))
    dir = os.getcwd()
    tdir = os.path.join(dir, "tex")
    ensure_dir(tdir)

    projdir = os.path.dirname(__file__)
    base, ext = os.path.splitext(args.filename)
    outfile = os.path.join(tdir, base + "-main" + ext)
    s = resource_string("quick_latex", "quick_template.tex")
    # print(e)
    print("current:", dir)
    with open(os.path.join(projdir, "quick_template.tex")) as f:
        t = Template(f.read())
        data = t.substitute(filename=args.filename)

        with open(outfile, "w") as outf:
            f.write(data)
