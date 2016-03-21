from subprocess import call
import argparse
from os.path import basename, dirname

parser = argparse.ArgumentParser()
parser.add_argument("file_ipynb")
args = parser.parse_args()
name = args.file_ipynb[:-6]

call(["jupyter", "nbconvert",  "--to", "latex", args.file_ipynb])

file = open(basename(name) + ".tex", "r")
lines = list(file)
file.close()
for i in range(len(lines)):
    if (lines[i].find("documentclass") != -1):
        lines.insert(i + 1, 
            r"\usepackage{cmap}" 
            + "\n" 
            + r"\usepackage[T2A]{fontenc}" 
            + "\n")
        break
file = open(basename(name) + ".tex", "w")
for line in lines:
    file.write(line)
file.close()

def latex_call():
    if (dirname(name) == ""):
        call(["pdflatex", 
              basename(name) + ".tex"])
    else:
        call(["pdflatex", 
        "-output-directory=" + dirname(name),
        basename(name) + ".tex"])

#calling for indexing & page numeration proposes
latex_call()
latex_call()

#clean latex
call(["rm", name + ".aux", name + ".log", name + ".out"])
#clean jupyter
call(["rm", "-rf", basename(name) + "_files", basename(name) + ".tex"])

print(dirname(name))