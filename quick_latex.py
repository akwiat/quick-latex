import argparse
import os
import shutil
import subprocess
import shlex
from string import Template
from pkg_resources import resource_string

parser = argparse.ArgumentParser(description='quick-compile a problem')
parser.add_argument('filename', type=str, help='name of the .tex file to compile')
parser.add_argument('-s', '--solutions', action='store_true')
# parser.add_argument('worksheet_name', nargs='?', type=str, help='name of the worksheet')
# parser.add_argument('--all', action='store_true', help='update all worksheets')

def ensure_dir(d):
    try:
        os.mkdir(d)
    except:
        pass

def compile(f):
    d, base = os.path.split(f)
    os.chdir(d)
    cmd = "pdflatex {} &> log.txt".format(shlex.quote(base))
    # cmd = "ls > log.txt"
    print("running:", cmd)
    r = subprocess.run(cmd, shell=True)
    print("output:", r.returncode)

def main():
    args = parser.parse_args()
    print("solutions? {}".format(args.solutions))
    print("filename: {}".format(args.filename))
    dir = os.getcwd()
    fullpath = os.path.join(dir, args.filename)
    f_dir, fname = os.path.split(fullpath)

    tdir = os.path.join(f_dir, "tex")
    ensure_dir(tdir)

    packagedir = os.path.dirname(__file__)
    base, ext = os.path.splitext(fname)
    outfile = os.path.join(tdir, base + "-main" + ext)
    s = resource_string("quick_latex", "quick_template.tex")
    # print(e)
    print("current:", dir)
    with open(os.path.join(packagedir, "quick_template.tex")) as f:
        t = Template(f.read())
        sflag = r'\solutiontrue' if args.solutions else r'\solutionfalse'
        data = t.substitute(filename=os.path.relpath(fullpath, tdir), solutions_flag = sflag)

        print("writing to:", outfile)
        with open(outfile, "w") as outf:
            outf.write(data)

    compile(outfile)

    pdir = os.path.join(f_dir, "pdf")
    ensure_dir(pdir)

    outbase, ext = os.path.splitext(outfile)
    shutil.move(outbase+".pdf", os.path.join(pdir, base + ".pdf"))

if __name__ == "__main__":
    main()
