'''Python Shell Improved/PSI/pyShell/shell.py/... 
You know what? i give up on these aliases.
The PSI is a shell program for python that
aims at making debugging and other short
tasks easier. It includes some quality-of-life
features and other things. importing it into
a project, you can access the projects functions
inside the PSI. And with that, enjoy!
@author: Elis Staaf
'''

import os
import functools
from string import Template

def printc(text=None, fg=None, bg=None): # Coloured text, works like the "Print" function, but with coloured text.
    print(f"\033[0;{fg};{bg}m{text}\033[0;37;40m")

def BWyZIW10LMfRwTDtIWsT(VAR):
    return VAR

def info():
    print('''
Python Shell Improved/PSI/pyShell/shell.py/... 
You know what? i give up on these aliases.
The PSI is a shell program for python that
aims at making debugging and other short
tasks easier. It includes some quality-of-life
features and other things. importing it into
a project, you can access the projects functions
inside the PSI. And with that, enjoy!
@author: Elis Stääf
''')

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

SoftwareVersion = Template("$major.$minor.$patch")
__ver__ = SoftwareVersion.substitute(major="1", minor="3", patch="11")

def clear(): 
    os.system("CLS")

prefab1 = {
    "name" : None,
    "code" : None
            }
prefab2 = {
    "name" : None,
    "code" : None
            }
prefab3 = {
    "name" : None,
    "code" : None
            }
prefab4 = {
    "name" : None,
    "code" : None
            }
prefab5 = {
    "name" : None,
    "code" : None
            }

nmspc = 0
name = 'undefined'
desc = 'undefined'
ln = 0
cd = "$"
standard="\033[0;37;40m"
error="\033[0;31;40m"
success="\033[0;32;40m"
prefabCount = 0

clear()
while True:
    ln += 1
    cmd = input(f"{ln} ")
    output = cmd
    outputSplit = output.split(" ")
    if 'shell.new' in outputSplit:
        name = 'undefined'
        desc = 'undefined'
        multi = ["Empty"]
        clear()
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
        if output > 0:
            ln = output - 1
        else:
            print(f"{error}Error: GOTO doesn't support numbers < 1{standard}")
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
        secelem = outputSplit[outputSplit.index('for')-len(outputSplit)+2]
        trielem = outputSplit[outputSplit.index('for')-len(outputSplit)+3]
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

        exec(f"""
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
""")
    elif "prefab" in outputSplit:
        nextelem = outputSplit[outputSplit.index('prefab')-len(outputSplit)+1]
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

        prefabList = [prefab1, prefab2, prefab3, prefab4, prefab5]
        prefabCount += 1
        if prefabCount > 4:
            print(f"{error}Error: you've exceeded the amount of prefabs [5] that you are allowed to have.{standard}")
        else:
            loadable = {
                "name" : nmf,
                "code" : (f"""class {output}
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
    {cmd20}""")}
            indexCount = 0
            for i in prefabList:
                if prefabList[indexCount]['name'] == None and prefabList[indexCount]['code'] == None:
                    prefabList[indexCount]['name'] = loadable['name']
                    prefabList[indexCount]['code'] = loadable['code']
                    print(f"{success}code successfully downloaded to prefab[{indexCount}]{standard}")
                    break
                else:
                    indexCount += 1
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
                print(f"{success}code succesfully uploaded from {output}")
                exec(contents)
        except IOError:
            print(f"{error}Error: couldn't read file " + contents) 
    elif 'preload' in outputSplit[0]:
        nextelem = outputSplit[outputSplit.index('preload')-len(outputSplit)+1]
        output = str(nextelem)
        indexCount = 0
        for i in prefabList:
            if output == prefabList[indexCount]['name']:
                exec(prefabList[indexCount]['code'])
                print(f"{success}code successfully uploaded from prefab[{indexCount}]{standard}")
                break
            else:
                print(f"{error}no code was found in prefab[{indexCount}] that matched with your request. Continuing search...{standard}")
                indexCount += 1
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
