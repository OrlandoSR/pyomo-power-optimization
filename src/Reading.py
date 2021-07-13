# Code for creating the lists given to Reusable.py from text files
# \t is tab and \n is new line
from Variables import *

path_to_line = "../res/3bus/line.txt"
path_to_bus = "../res/3bus/bus.txt"
path_to_generator = "../res/3bus/gen.txt"

with open(path_to_line) as f_line:
    linecontent = f_line.readlines()

with open(path_to_bus) as f_bus:
    buscontent = f_bus.readlines()

with open(path_to_generator) as f_gen:
    gencontent = f_gen.readlines()

# Recieves the list of string the original part to replace and the replacement return the modified list
def cleanList(list, orig, repl):
    result = []
    for i in list:
        result.append(i.replace(orig, repl))

    return result


buscontent = cleanList(buscontent, "\n", "")
buscontent = cleanList(buscontent, "\t", ",")

gencontent = cleanList(gencontent, "\n", "")
gencontent = cleanList(gencontent, "\t", ",")

linecontent = cleanList(linecontent, "\n", "")
linecontent = cleanList(linecontent, "\t", ",")

print(buscontent)
print(linecontent)
print(gencontent)

# Take the cleaned list of strings and create an appropiate object for each
