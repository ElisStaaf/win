import os
import functools
import inspect as ins
from rich import *
from time import sleep
from dataclasses import dataclass

first: bool = True
ln: int = 0
lnid: dict = {}
program: list = []
sterr: bool = False

def clear() -> None:
    if os.name == "nt":
        os.system("cls")

def onclear(func): # Set timer

    @functools.wraps(func)

    def wrapper_onclear(*args, **kwargs):
        clear()
        func(*args, **kwargs)
    return wrapper_onclear

@onclear
def onready() -> None:
    print("""
[bold sea_green2]
███    ██ ███████  ██████  ██    ██ ███████ ██   ██ 
████   ██ ██      ██    ██ ██    ██ ██       ██ ██  
██ ██  ██ █████   ██    ██ ██    ██ █████     ███   
██  ██ ██ ██      ██    ██  ██  ██  ██       ██ ██  
██   ████ ███████  ██████    ████   ███████ ██   ██ 
[/bold sea_green2]
NeoVex is a python IDE based on the original Vex. It provides more powerful features
and is really great! Commands: [bold sea_green2]start:[/bold sea_green2] - start file, 
[bold sea_green2]end:[/bold sea_green2] - end file, [bold sea_green2]exit:[/bold sea_green2] - exit NeoVex, [bold sea_green2]set:[/bold sea_green2] - Access settings.
""")

with open(r"C:\Users\eliss\OneDrive\Desktop\scripts\autoimports.nvx", "r") as auim:
    contents = auim.read()
    exec(contents)

onready()
while True:
    ln += 1
    unprocessedinput = input(f"{ln} ")
    output = unprocessedinput
    token = output.split(" ")
    lnid[ln] = token
    if first == True and "start:" not in token[0]:
        sterr = True
    elif "func" in token[0]:
        nextelem = token[token.index('func')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""def {output}
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "class" in token[0]:
        nextelem = token[token.index('class')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""class {output}
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "namespace" in token[0]:
        nextelem = token[token.index('namespace')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""class {output}
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "if" in token[0]:
        nextelem = token[token.index('if')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""if {output}
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "elif" in token[0]:
        nextelem = token[token.index('elif')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""elif {output}
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "else:" in token[0]:
        nextelem = token[token.index('else')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""else:
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "for" in token[0]:
        nextelem = token[token.index('for')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""for {output}
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "with" in token[0]:
        nextelem = token[token.index('with')-len(token)+1]
        output = str(nextelem)
        func = []
        while True:
            cmd = input("")
            fcmd = str(cmd)
            if fcmd == "end:":
                ffunc = "".join(func)
                exec(f"""with {output}
{ffunc}""")
                break
            else:
                func.append(fcmd)
    elif "GOTO" in token[0]: 
        nextelem = token[token.index('GOTO')-len(token)+1]
        output = int(nextelem)
        program.append(str(lnid[output]))
    elif "end:" in token[0]:
        try:
            fprogram = "".join(program)
            if sterr != True:
                exec(fprogram)
            else:
                print("[bold red]SyntaxError: Missing \"start:\" at line 1.[/bold red]")
        except SyntaxError as err:
            print(f"[bold red]SyntaxError: Couldn't process program.[/bold red]")
        finally:
            program = []
            ln = 0
    elif "exit:" in token[0]:
        break
    elif "set:" in token[0]:
        print("""
Settings: 
[bold sea_green2]$autoimports[/bold sea_green2] - change automatic imports
""")
        setter = input("""
""")
        raw = setter
        output = raw.split(" ")
        if "$autoimports" in output:
            imports = input("Type in all autoimports separated by a semicolon (;)\n>>> ")
            with open(r"C:\Users\eliss\OneDrive\Desktop\scripts\autoimports.nvx", "w") as auim:
                auim.write(imports)
    else:
        program.append(output)
    first = False
