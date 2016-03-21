from subprocess import call
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_ipynb")
args = parser.parse_args()
name = args.file_ipynb[:-6]

print(name)
call(["jupyter", "nbconvert", "--to", "latex", args.file_ipynb])

file = open(name + ".tex", "r")
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
file = open(name + ".tex", "w")
for line in lines:
	file.write(line)
file.close()

call(["pdflatex", name + ".tex"])
call(["rm", name + ".aux", name + ".log", name + ".out", name + ".tex"])
call(["rm", "-rf", name + "_files"])