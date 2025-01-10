
#!/bin/python3

import os
import functools
from time import sleep
import random

def printc(text=None, fg=None, bg=None): # Coloured text, works like the "Print" function, but with coloured text.
    print(f"\033[0;{fg};{bg}m{text}\033[0;37;40m")

def BWyZIW10LMfRwTDtIWsT(VAR):
    return VAR

def GhorT278Drty(func): # GhorT278Drty mode, incredibly useful tool

    @functools.wraps(func)

    def wrapper_GhorT278Drty(*args, **kwargs):
        args_repr = [repr(a) for a in args]

        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]

        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Calling {func.__name__}({signature})")

        value = func(*args, **kwargs)

        print(f"{func.__name__}() returned {repr(value)}")

        return value
        
    return wrapper_GhorT278Drty

class SoftwareVersion(tuple):

    __slots__ = ()
    fields = "major", "minor", "patch"

    def __new__(cls, major, minor, patch):
        return tuple.__new__(cls, (major, minor, patch))

    def __repr__(self):
        fields = (f"{fld}={val}" for fld, val in zip(self.fields, self))
        return f"{str(self.__class__.__name__)}({', '.join(fields)})"

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    major = property(lambda self: self[0])
    minor = property(lambda self: self[1])
    patch = property(lambda self: self[2])
    # ! NOTE: You HAVE to list all three properties
    # ! when using this class, you HAVE to.  

class shellpythonver(SoftwareVersion):
    '''Shellpythonver'''
__ver__ = shellpythonver(1,3,0)

def clearShell64(): # clearShell64 shell
    if os.name == 'nt': 
        _ = os.system('cls')

def readFile64(filename=None):# Read file
    try:
        with open(filename, 'r') as f: # Char 'r' = read
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: couldn't read file " + filename)

def invFile64(filename=None):# Read file
    try:
        with open(filename, 'r') as f: # Char 'r' = read
            contents = f.read()
            print(contents)
            exec(contents)
    except IOError:
        print("Error: couldn't read file " + filename)

nmspc = 0
name = 'undefined'
desc = 'undefined'
ln = 0
clearShell64()
cd = "$"
standard="\033[0;37;40m"
system="\033[0;31;40m"
loadable = {
    "code": None,
    "name": None
            }

while True:
    ln += 1
    cmd = input(f"{ln} ")
    output = cmd
    outputSplit = output.split(" ")
    if 'shell.new' in outputSplit:
        name = 'undefined'
        desc = 'undefined'
        multi = ["Empty"]
        clearShell64()
        ln = 0
        cd = "$"
    elif 'shell.exit' in outputSplit:
        quit()
    elif 'shell.name' in outputSplit:
        nextelem = outputSplit[outputSplit.index('shell.name')-len(outputSplit)+1]
        output = str(nextelem)
        name = output
    elif 'shell.desc' in outputSplit:
        nextelem = outputSplit[outputSplit.index('shell.desc')-len(outputSplit)+1]
        output = str(nextelem)
        desc = output
    elif 'shell.info' in outputSplit:
        print(f'''name:
{name}
desc: 
{desc}''') 
    elif 'GOTO' in outputSplit:
        nextelem = outputSplit[outputSplit.index('GOTO')-len(outputSplit)+1]
        output = int(nextelem)
        ln = output - 1
    elif output == 'SOFTWAREVERSION':
        print(__ver__)
    elif 'col.new' in outputSplit:
        cmd = input(":: ")
    elif 'semicol.new' in outputSplit:
        nextelem = outputSplit[outputSplit.index('semicol.new')-len(outputSplit)+1]
        output = int(nextelem)
        for i in range(output):
            cmd = input(";; ")
            cmdSplit = cmd.split(" ")
            if 'semicol.break' in cmdSplit:
                break
    elif 'func' in outputSplit:
        nextelem = outputSplit[outputSplit.index('func')-len(outputSplit)+1]
        output = str(nextelem)
        cmd2 = input(f"    ")
        cmd3 = input(f"    ")
        cmd4 = input(f"    ")
        cmd5 = input(f"    ")
        exec(f"""def {output}
    {cmd2}
    {cmd3}
    {cmd4}
    {cmd5}""")
    elif 'GhorT278Drty' in outputSplit:
        nextelem = outputSplit[outputSplit.index('GhorT278Drty')-len(outputSplit)+1]
        output = str(nextelem)
        cmd2 = input(f"    ")
        cmd3 = input(f"    ")
        cmd4 = input(f"    ")
        cmd5 = input(f"    ")
        exec(f"""@GhorT278Drty
def {output}
    {cmd2}
    {cmd3}
    {cmd4}
    {cmd5}""")
    elif "if" in outputSplit:
        nextelem = outputSplit[outputSplit.index('if')-len(outputSplit)+1]
        output = str(nextelem)
        cmd2 = input(f"    ")
        cmd3 = input(f"    ")
        cmd4 = input(f"    ")
        cmd5 = input(f"    ")
        exec(f"""if {output}
    {cmd2}
    {cmd3}
    {cmd4}
    {cmd5}""") 
    elif "while" in outputSplit:
        nextelem = outputSplit[outputSplit.index('while')-len(outputSplit)+1]
        output = str(nextelem)
        cmd2 = input(f"    ")
        cmd3 = input(f"    ")
        cmd4 = input(f"    ")
        cmd5 = input(f"    ")
        exec(f"""while {output}
    {cmd2}
    {cmd3}
    {cmd4}
    {cmd5}""")
    elif "for" in outputSplit:
        nextelem = outputSplit[outputSplit.index('for')-len(outputSplit)+1]
        secelem = outputSplit[outputSplit.index('with')-len(outputSplit)+2]
        trielem = outputSplit[outputSplit.index('with')-len(outputSplit)+3]
        output = str(nextelem)
        output2 = str(secelem)
        output3 = str(trielem)
        cmd2 = input(f"    ")
        cmd3 = input(f"    ")
        cmd4 = input(f"    ")
        cmd5 = input(f"    ")
        exec(f"""for {output} {output2} {output3}
    {cmd2}
    {cmd3}
    {cmd4}
    {cmd5}""")
    elif "with" in outputSplit:
        nextelem = outputSplit[outputSplit.index('with')-len(outputSplit)+1]
        output = str(nextelem)
        cmd2 = input(f"    ")
        cmd3 = input(f"    ")
        cmd4 = input(f"    ")
        cmd5 = input(f"    ")
        exec(f"""with {output}
    {cmd2}
    {cmd3}
    {cmd4}
    {cmd5}""")
    elif "namespace" in outputSplit:
        nextelem = outputSplit[outputSplit.index('namespace')-len(outputSplit)+1]
        output = str(nextelem)
        cmd2 = input(f"    ")
        cmd3 = input(f"    ")
        cmd4 = input(f"    ")
        cmd5 = input(f"    ")
        cmd6 = input(f"    ")
        cmd7 = input(f"    ")
        cmd8 = input(f"    ")
        cmd9 = input(f"    ")
        cmd10 = input(f"    ")
        cmd11 = input(f"    ")
        cmd12 = input(f"    ")
        cmd13 = input(f"    ")
        cmd14 = input(f"    ")
        cmd15 = input(f"    ")
        cmd16 = input(f"    ")
        cmd17 = input(f"    ")
        cmd18 = input(f"    ")
        cmd19 = input(f"    ")
        cmd20 = input(f"    ")
        
        nmspc += 1

        nm1 = output.split("(")
        nm2 = output.split(":")
        nmf = nm2[0]

        loadable = {
    "code": (f"""
class {output}
    {cmd2}
    {cmd3}
    {cmd4}
    {cmd5}
    {cmd6}
    {cmd7}
    {cmd8}
    {cmd9}
    {cmd10}
    {cmd11}
    {cmd12}
    {cmd13}
    {cmd14}
    {cmd15}
    {cmd16}
    {cmd17}
    {cmd18}
    {cmd19}
    {cmd20}
"""),
"name": nmf
    }
        exec(loadable['code'])
    elif 'invoke' in outputSplit:
        nextelem = outputSplit[outputSplit.index('invoke')-len(outputSplit)+1]
        output = str(nextelem)
        exec(output)
    elif 'load' in outputSplit:
        nextelem = outputSplit[outputSplit.index('load')-len(outputSplit)+1]
        output = str(nextelem)
        try:
            with open(output, 'r') as f: # Char 'r' = read
                contents = f.read()
                print(contents)
                exec(contents)
        except IOError:
            print("Error: couldn't read file " + contents) 
    elif 'preload' in outputSplit[0]:
        nextelem = outputSplit[outputSplit.index('preload')-len(outputSplit)+1]
        output = str(nextelem)
        if output == loadable['name']:
            exec(loadable['code'])
            sleep(4.2921)
            bytecount = random.randint(90,500)
            print(f"{system}preload successfully imported ({bytecount} bytes){standard}")
        else:
            print(f"{system}Shellpython doesn't what the \"{output}\" preload is.{standard}")
            quit()
    elif cd in outputSplit[0]:
        nextelem = outputSplit[outputSplit.index(cd)-len(outputSplit)+1]
        output = str(nextelem)
        if output == 'multi':
            nextelem = outputSplit[outputSplit.index('multi')-len(outputSplit)+1]
            output = int(nextelem)
            elem2 = outputSplit[outputSplit.index('multi')-len(outputSplit)+2]
            multi = []
            j = 0
            for i in range(output):
                j += 1
                multi.append(f"{j}")
        if output == 'req':
            nextelem = outputSplit[outputSplit.index('req')-len(outputSplit)+1]
            var = str(nextelem)
            BWyZIW10LMfRwTDtIWsT(var)
    else:
        exec(output) 

# End of file. 