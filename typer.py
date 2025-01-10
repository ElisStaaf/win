# Create errors
class BaseTyperError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class TyperImportError(BaseTyperError):
    pass

class ChangeValueError(BaseTyperError):
    pass

class OutdatedError(BaseTyperError):
    pass

#Import modules with an exception:
try:
    import sys
    import typing as tg
    import types as ty
    import threading
    import time
except ImportError as err:
    raise TyperImportError(f"TyperImportError: {err}")

sysversion = [str(sys.version_info.major), str(sys.version_info.minor)]
sysversion = ".".join(sysversion)
sysversion = float(sysversion)

if sysversion < 3.12:
    raise OutdatedError('''
You are running this module; a module made for python 3.12 and up, on a python 
version before python 3.12. Therefore, this module will not run on your version. If you 
want to use this module, please visit https://www.python.org/downloads/ 
to download the latest version of python.                    
''')

vardict = {}

type flint = float|int
type char = chr

class construct:
    '''
    * .HowToUse
    : {name(use param?)} = construct({name}, {types}, {value}, {auto=True})
    * .WhyYouShouldUse
    : Provides more familiar typing, and stores your value for 
    later if you don't wanna declare it now.
    '''

    def __init__(self, name:str, types:any, value:any, auto:bool=True) -> None:
        self.name = name
        self.types = types
        self.value = value
        self.auto = auto

        self.name = f"{self.name} : {self.types}"
        vardict[self.name] = self.value
        if self.auto == True:
            self.packaged = f"{self.name}={self.value}"
            exec(self.packaged) 

    def pakg(self):
        if self.auto != True:
            exec(self.packaged)
