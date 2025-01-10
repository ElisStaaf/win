#                                              MMMMMMMM               MMMMMMMM                             dddddddd
#                                              M:::::::M             M:::::::M                             d::::::d
#                                              M::::::::M           M::::::::M                             d::::::d
#                                              M:::::::::M         M:::::::::M                             d:::::d 
#    ppppp   pppppppppyyyyyyy           yyyyyyyM::::::::::M       M::::::::::M   ooooooooooo       ddddddddd:::::d 
#    p::::ppp:::::::::py:::::y         y:::::y M:::::::::::M     M:::::::::::M oo:::::::::::oo   dd::::::::::::::d 
#    p:::::::::::::::::py:::::y       y:::::y  M:::::::M::::M   M::::M:::::::Mo:::::::::::::::o d::::::::::::::::d 
#    pp::::::ppppp::::::py:::::y     y:::::y   M::::::M M::::M M::::M M::::::Mo:::::ooooo:::::od:::::::ddddd:::::d 
#     p:::::p     p:::::p y:::::y   y:::::y    M::::::M  M::::M::::M  M::::::Mo::::o     o::::od::::::d    d:::::d 
#     p:::::p     p:::::p  y:::::y y:::::y     M::::::M   M:::::::M   M::::::Mo::::o     o::::od:::::d     d:::::d 
#     p:::::p     p:::::p   y:::::y:::::y      M::::::M    M:::::M    M::::::Mo::::o     o::::od:::::d     d:::::d 
#     p:::::p    p::::::p    y:::::::::y       M::::::M     MMMMM     M::::::Mo::::o     o::::od:::::d     d:::::d 
#     p:::::ppppp:::::::p     y:::::::y        M::::::M               M::::::Mo:::::ooooo:::::od::::::ddddd::::::dd
#     p::::::::::::::::p       y:::::y         M::::::M               M::::::Mo:::::::::::::::o d:::::::::::::::::d
#     p::::::::::::::pp       y:::::y          M::::::M               M::::::M oo:::::::::::oo   d:::::::::ddd::::d
#     p::::::pppppppp        y:::::y           MMMMMMMM               MMMMMMMM   ooooooooooo      ddddddddd   ddddd
#     p:::::p               y:::::y                                                                                
#     p:::::p              y:::::y                                                                                 
#     p:::::::p           y:::::y                                                                                  
#     p:::::::p          y:::::y                                                                                   
#     p:::::::p         yyyyyyy                                                                                    
#     ppppppppp                    
                                                                                                     
'''                                                                                                           
This is a collection of two modules that i made; decor and pyLauncher, but i 
also added more features that weren't originally
in any of these modules.
Please take a look at the function and class list below:

:``PluginMod()``:
    :``@register`` - register function as a plugin
    :``log()`` - view all current plugins
:``Pyfiles()``:
    :``create_file(filename)`` - create file
    :``write_file(filename, text)`` - create and write file
    :``read_file(filename)`` - read file, then print out its contents
    :``append_file(filename, text) ``- append file, as in add text to the end
    :``rename_file(filename, new_filename)`` - rename file
    :``delete_file(filename) - delete file``
:``Decor()``:
    :``@do_twice`` - Deprecated function
    :``@timer`` - set a timer
    :``@debug`` - debug a specific function
    :``@slow_down`` - slow down a specific function
    :``@repeat(num_times)`` - repeat a function a set aount of times, leave empty for value 2
    :``@count_calls`` - counts how many times something ha been called
    :``@singleton`` - store function as singleton
    :``@cache`` - hold info
:``Cryptography()``:
    :``encrypt(filename)`` - Encrypts files (Use at your own risk)
    :``decrypt(filename)`` - Decrypts encrypted files
:``Console()``:
    :``printc(text, fg, bg)`` - coloured text, really awesome!
    :``printf(text, fs)`` - fontstyles to your text
    :``printcf(text, fs, fg, bg)`` - text with fontstyles and colours!
    :``clear()`` - clear shell
:``Codecs()``:
    :``rot13_encode(s)`` - encode a string using the rot13 encoding system!
    :``rot13_decode(s)`` - decode a string using the rot13 decoding system!
    :``obfuscator(code)`` - Deprecated function
    :``deobfuscator(code)`` - Deprecated function
    :``spws()`` - Password system, stands for Sub-PassWord System.
    :``binargs()`` - Makes a binary-like object out of 4 arguments.
:``Html()``:
    :``web_scraper(url)`` - Tool that scrapes the web so that you can gather info! Beware though, it's not fast
    :``html_scraper(url)`` - Same as the webscraper, but it scrapes all of the code.
:``Compiler()``:
    :``compile_exec(filename, object)`` - Compiles and executes.

Also, please use the ``from pyMod import *`` function
when importing pyMod. If you don't know, it imports everything
in pyMod, but you dont need to use the "pyMod." prefix to 
access functions. 

Some functions in this module may be bugged 
but thats hopefully okay. We don't need A+ code here, we need 
functioning code, which there hopefully is in this module. 
Also, the author of this module isn't liable for any, uhh, 
crimes commited using this software. But asides from that, enjoy!
'''

class Locals():
    '''
    Base class for local functions
    in pyMod, these are not meant to
    be used in other modules, but
    you can ofcourse try! (don't) 
    '''

    class obj(): 
        '''Basic message class'''

        def __init__(self, string):
            self.string = string 
        
        def __str__(self):
            return self.string

        def __repr__(self):
            return 'Object: {}'.format(self.string)
            
        def __add__(self, other):
            return self.string + other

# Create errors
class BasePMError(Exception):
    """Base class for pyMod errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class OutdatedError(BasePMError):
    '''
    If user is running a version 
    of python before python 3,
    this error is raised.
    '''
    pass

class DeprecatedError(BasePMError):
    '''
    If user tries to run
    a deprecated function,
    this error is raised.
    '''
    pass

class VoidError(BasePMError):
    '''
    If no value is inputted
    in a function that needs
    a value, this error
    is raised.
    '''
    pass

class SupportError(BasePMError):
    '''
    If pyMod doesn't support a 
    specific function, pyMod 
    raises this error.
    '''
    pass

class FatalError(BasePMError):
    '''
    Base class for fatal errors
    in pyMod. If this error
    is raised, you are in
    big trouble.
    '''
    pass

# Non class-related errors:
FileError = OSError
PermError = PermissionError
ModuleError = ModuleNotFoundError

__errors__ = [ 
    BasePMError,
    OutdatedError,
    DeprecatedError,
    VoidError,
    SupportError,
    FatalError,
    FileError,
    PermError,
    ModuleError,
]
'''A list of all errors in pyMod'''

# Create warnings:
class BasePMWarning(Warning):
    '''Base class for warnings in pyMod.'''

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class GuessedValueWarning(BasePMWarning):
    '''
    Warning that occurs when no value is specified 
    under specific conditions.
    '''

__warnings__ = [ 
    BasePMWarning,
    GuessedValueWarning,
]
'''A list of all warnings in pyMod'''

# Create logic surrounding versions
class SoftwareVersion(tuple):
    """
    Class for storing data about versions in pyMod
    """
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
    # NOTE: You HAVE to list all three properties
    # when using this class, you HAVE to. 

class PyModVersion(SoftwareVersion):
    '''
    pyMod version class
    '''

# Using this import model, we can
# minimize the damages if one module
# doesn't work. It only gives an error
# to the classes that use the module.
# (except for sys, ofcourse.)
try:
    import sys # system module
except ImportError:
    raise FatalError("CRITICAL PYMOD ERROR: FAILED TO IMPORT SYSTEM MODULE")
try:
    import functools # decor
    import time # timer decor 
    decor_error = False
except ImportError:
    decor_error = True
try:
    import os # access files, clear shell
    file_error = False
    console_error = False   
except ImportError:
    file_error = True
    console_error = True
try:
    import warnings # Warnings
    warnings_error = False
except ImportError:
    warnings_error = True
try:
    from codecs import encode, decode # rot13
    from cryptography.fernet import Fernet # encryption tool
    import random
    codecs_error = False
except ImportError:
    codecs_error = True
try:
    from urllib.request import urlopen # Web scraping tool
    from bs4 import BeautifulSoup # Web scraping tool
    html_error = False
except ImportError:
    html_error = True
try:
    from cryptography.fernet import Fernet # encryption tool
    cryptography_error = False
except ImportError:
    cryptography_error = True


# Some info about the module:
__author__ = 'Elis Staaf' 
'''pyMod author'''
__ver__ = PyModVersion(1, 5, 1)
'''pyMod version'''
__pyver__ = sys.version_info.major
'''Python version'''
__all__ = [ # For easy access to viewing the classes in your own project, print this list.
'SoftwareVersion',
'PluginMod',
'Pyfiles',
'Decor',
'Cryptography',
'Console',
'Codecs',
'Html',
'pyModInfo',
]# More classes will probably be added soon.
'''A list of all classes in pyMod'''

# Check if user is running an outdated version of python,
# if so, we print a helpful warning.
if __pyver__ < 3: 
    raise OutdatedError('''
OutdatedError: You are running this module; a module made for python 3 and up, on a python 
version before python 3. Therefore, this module will not run on your version. If you 
want to use this module, please visit https://www.python.org/downloads/ 
to download the latest version of python.                    
''')

class PluginMod():
    '''
    Base class for the ``PluginMod`` plugin architecture in pyMod.
    To use, please register a function using the ``@register``
    function.
    
    For example:

        >>> from pyMod import *
        >>> pl = PluginMod
        >>> @pl.register # Register a function
        >>> def greet(name): # Define function
        >>>     greeting = f"Hello, {name}!"
        >>>     return greeting
        >>> pl.log() # Print the plugins
        {'greet': <function greet at {memory adress}>}
    '''

    PLUGINS = {} # Declare the PLUGINS dictionary
    '''
    Dictionary to hold the plugins from the
    ``PluginMod`` architecture, please use the
    ``@register`` function to register a function
    as a plugin.
    '''

    def register(func): # Register for plugin
        super().PLUGINS[func.__name__] = func
        return func 
    
    def log(): # Check the plugins
        return super().PLUGINS
    
class Pyfiles(): 
    '''
    Base class for filemanaging in pyMod.
    Pyfiles makes it easy to manage 
    files trough python.

    For example:

        >>> from pyMod import *
        >>> pf = Pyfiles
        >>> pf.write_file("HelloWorld.py", "print(\"Hello, world!\")")
        File HelloWorld.py written successfully.
    
    HelloWorld.py:

        >>> print("Hello, world!)
    '''

    if file_error == True:
        raise ModuleError('''The necessary modules needed to use this pyMod class were
unable to be found.''')

    def create_file(filename=None): # Create file 
        if filename == None:
            raise VoidError('''
VoidError: no value was inputted, so pyMod
can't read your program.
''')
        else:
            try:
                with open(filename, 'w') as f: # Char 'w' = create and write
                    return("File " + filename + " created successfully.")
            except FileError:
                print("FileError: couldn't create file " + filename)

        def write_file(filename=None, text=None): # Create and write file
            if filename == None:
                raise VoidError('''
VoidError: no value was inputted, so pyMod
can't read your program.
''')
            else:
                try:
                    with open(filename, 'w') as f: # Char 'w' = create and write
                        f.write(text)
                        return("File " + filename + " written succesfully.")
                except FileError:
                    print("FileError: couldn't write file " + filename)

    def read_file(filename=None):# Read file
        if filename == None:
            raise VoidError('''
VoidError: no value was inputted, so pyMod
can't read your program.
''')
        else:
            try:
                with open(filename, 'r') as f: # Char 'r' = read
                    contents = f.read()
                    return(contents)
            except FileError:
                print("FileError: couldn't read file " + filename)

    def append_file(filename=None, text=None): # Append file
        if filename == None or text == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            try:
                with open(filename, 'a') as f: # Char 'a' = append
                    f.write(text)
                return("Text appended to file " + filename + " successfully.")
            except FileError:
                print("FileError: couldn't append to file " + filename)

    def rename_file(filename=None, new_filename=None): # Rename file
        if filename == None or new_filename == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            try:
                os.rename(filename, new_filename) # Call os.rename function to rename file
                return("File " + filename + " renamed to " + new_filename + " successfully.")
            except FileError:
                print("FileError: couldn't rename file " + filename)

    def delete_file(filename=None): # Delete file
        if filename == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            try:
                    try:
                        os.remove(filename) # Call os.remove function to delete file
                        return("File " + filename + " deleted successfully.")
                    except PermError:
                        print("")
            except FileError:
                print("FileError: couldn't delete file " + filename)

class Decor():  
    '''
    Base class for pyMod decor.
    To use, use the @{function name}
    command.
    
    For example:
    
        >>> from pyMod import *
        >>> dc = Decor
        >>> @dc.repeat(5)
        >>> def greet(name):
        >>>     print(f"Hello, {name}!")
        >>> greet("world")
        Hello, world!
        Hello, world!
        Hello, world!
        Hello, world!
        Hello, world!
        '''

    if decor_error == True:
        raise ModuleError('''The necessary modules needed to use this pyMod class were
unable to be found.''')

# The do twice function is deprecated
# because you can do the exact same
# thing with the ``@repeat``
# function. If you try to run this
# function, you will get a 
# DeprecatedError.
    def do_twice(func): 
        raise DeprecatedError('''
The do_twice function is deprecated,
instead, use the repeat function
to repeat twice.
''')

    def timer(func): # Set timer

        @functools.wraps(func)

        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter() 
            value = func(*args, **kwargs) # Set timer to the correct value
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__}() in {run_time:.4f} secs") # Print runtime
            return value
        return wrapper_timer

    def debug(func): # Debug mode, incredibly useful tool

        @functools.wraps(func)

        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]

            kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]

            signature = ", ".join(args_repr + kwargs_repr)

            print(f"Calling {func.__name__}({signature})")

            value = func(*args, **kwargs)

            print(f"{func.__name__}() returned {repr(value)}")

            return value
        
        return wrapper_debug

    def slow_down(_func=None, *, rate=1): # Declare slowdown rate
        def decorator_slow_down(func):
            @functools.wraps(func)
            def wrapper_slow_down(*args, **kwargs):
                time.sleep(rate) # The sleep function is set to "rate"
                return func(*args, **kwargs)
            return wrapper_slow_down

        if _func is None: # Check if "_func" value exists
            return decorator_slow_down
        else:
            return decorator_slow_down(_func)

    def repeat(_func=None, *, num_times=2): # Repeat, if left empty it is set to 2
        def decorator_repeat(func):
            @functools.wraps(func)
            def wrapper_repeat(*args, **kwargs):
                for _ in range(num_times): # Make a variable and set it to the "value" range
                    value = func(*args, **kwargs)
                return value
            return wrapper_repeat
        if _func is None: # If "_func" exists, set repeat to that value
            return decorator_repeat
        else:
            return decorator_repeat(_func)

    def count_calls(func): # Count how many times a function has been called
        @functools.wraps(func)
        def wrapper_count_calls(*args, **kwargs):
            wrapper_count_calls.num_calls += 1
            print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}()") # Print the num_calls value.
            return func(*args, **kwargs)
        wrapper_count_calls.num_calls = 0
        return wrapper_count_calls
   
    def singleton(cls): # Store function as singleton
        @functools.wraps(cls)
        def wrapper_singleton(*args, **kwargs):
            if wrapper_singleton.instance is None:
                wrapper_singleton.instance = cls(*args, **kwargs)
            return wrapper_singleton.instance
        wrapper_singleton.instance = None
        return wrapper_singleton

    def cache(func): # Hold cache value
        @functools.wraps(func)
        def wrapper_cache(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())
            if cache_key not in wrapper_cache.cache:
                wrapper_cache.cache[cache_key] = func(*args, **kwargs)
            return wrapper_cache.cache[cache_key]
        wrapper_cache.cache = {}
        return wrapper_cache
    
    # This is a test function,
    # but im leaving it here
    # incase someone wants to
    # use it.
    @timer
    def waste_time(self, num_times): # waste time
        for _ in range(num_times):
            sum([number**2 for number in range(self.max_num)])

class Cryptography():
    '''
    Base class for cryptography in pyMod.
    USE AT OWN RISK. Easily encrypt
    and decrypt files!

    For example:

        >>> from pyMod import *
        >>> pf = Pyfiles
        >>> cg = Cryptography
        >>> cg.encrypt("HelloWorld.txt")
        >>> pf.read_file("HelloWorld.txt"):
        VQHF9Q1EIwMCqUQYuZPat3GrfhmTeEhgGfwehBTHwD422tzxpO
    '''

    if cryptography_error == True:
        raise ModuleError('''The necessary modules needed to use this pyMod class were
unable to be found.''')

    def encrypt(filename=None): # Encrypt a file
        if filename == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            try:
                key = Fernet.generate_key() # Generate a fernet key
                with open("EncryptionKey", "wb") as key_dir:
                    key_dir.write(key)
                try:
                    with open(filename, "rb") as target:
                        contents = target.read()
                    try:
                        contents_encrypted = Fernet(key).encrypt(contents)
                        with open(filename, "wb") as target:
                            target.write(contents_encrypted) # And... Encrypted!
                    except FileError():
                        print("Couldn't encrypt target file.")
                except FileError:
                    print("FileError: Couldn't find target file.")
            except FileError:
                print("FileError: Couldn't make key.")

    def decrypt(filename=None): # Decrypt a file
        if filename == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            try:
                with open("EncryptionKey", "rb") as key_dir: # Get the key
                    key = key_dir.read()
                try:
                    with open(filename, "rb") as target:
                        contents = target.read()
                    try:
                        contents_decrypted = Fernet(key).decrypt(contents)
                        with open(filename, "wb") as target: 
                            target.write(contents_decrypted) # And... Decrypted! 
                    except FileError:
                        print("FileError: Couldn't decrypt target file.")
                except FileError:
                    print("FileError: Couln't find target file.")
            except FileError:
                print("FileError: Couldn't find key.")

    # FIXME: Catshift is starting to crumble.
    def catshift(file=None, cat=None):
        if file == None or cat == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            key = Fernet.generate_key()
            cat_key = Fernet(key).encrypt(cat)
            print(f"Your key is {cat_key}, don't lose it!")
            try:
                with open("catkey", "wb") as cat_dir:
                    cat_dir.write(cat_key)
                with open(file, "rb") as target:
                    contents = target.read()
                contents_catted = Fernet(cat_key).encrypt(contents)
                with open(file, "wb") as target:
                    target.write(contents_catted)
            except FileError:
                print("Error, couldn't get the neccessary files.")
    
    # FIXME: Catshift is starting to crumble.
    def catdeshift(file, cat):
        if file == None or cat == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            try:
                with open("catkey", "rb") as cat_dir:
                    cat_key = cat_dir.read()
                if cat == cat_key:
                    with open(file, "rb") as target:
                        contents = target.read()
                    contents_decatted = Fernet(cat).decrypt(contents)
                    with open(file, "wb") as target:
                        target.write(contents_decatted)
            except FileError:
                print("Error, couldn't get the neccessary files.")

class Console():  
    '''
    Base class for pyMod terminal occurences.
    With this class, you can both write
    coloured text, styled text and you
    can clear the terminal!

    For example:

        >>> from pyMod import *
        >>> from time import sleep
        >>> cn = Console
        >>> cn.printcf("Hello, world!", 1, 35, 40)
        𝙃𝙚𝙡𝙡𝙤, 𝙬𝙤𝙧𝙡𝙙! 
        >>> sleep(1)
        >>> clear()
        (empty)
    '''

    if console_error == True:
        raise ModuleError('''The necessary modules needed to use this pyMod class were
unable to be found.''')

    def printc(text=None, fg=None, bg=None): # Coloured text, works like the "Print" function, but with coloured text.
        if text == None or fg == None or bg == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            print(f"\033[0;{fg};{bg}m{text}\033[0;37;40m")

    def printf(text=None, fs=None): # Text with fontstyles!!
        if text == None or fs == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            print(f"\033[{fs};37;40m{text}\033[0;37;40m")

    def printcf(text=None, fs=None, fg=None, bg=None): # Add not only coloured text, but also fontstyles
        if text == None or fg == None or bg == None or fs == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            print(f"\033[{fs};{fg};{bg}m{text}\033[0;37;40m")

    def clear(): # clear shell
        if os.name == 'nt': 
            _ = os.system('cls')

class Codecs():
    '''
    Base class for encoding with pyMod.
    The codecs class provides
    an easy way to encode strings
    of text in python!

    For example:

       >>> from pyMod import *
       >>> cd = Codecs
       >>> cd.rot13_encode("Hello, world!")
       Uryyb, jbeyq!
       >>> cd.rot13_decode("Uryyb, jbeyq!")
       Hello, world!
    '''

    if codecs_error == True:
        raise ModuleError('''The necessary modules needed to use this pyMod class were
unable to be found.''')

    def rot13_encode(s=None): # Encode a string using rot13
        if s == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            encoded = encode(s, 'rot13')
            return(encoded)

    def rot13_decode(s=None): # Decode a string using rot13
        if s == None:
            raise VoidError('''
    VoidError: no value was inputted, so pyMod
    can't read your program.
    ''')
        else:
            decoded = decode(s, 'rot13')
            return(decoded)

# The obfuscation functions are deprecated, but im
# leaving them here as an artifact. If you try to
# run these functions, you will get a
# DeprecatedError.
    def obfuscate(code=None): 
        raise DeprecatedError('''
The obfuscate function is deprecated because
it was slow, tedious, and buggy.
''')
    
    def deobfuscate(code=None): 
        raise DeprecatedError('''
The deobfuscate function is deprecated because
it was slow, tedious, and buggy.
''')

    def spws(): # Password system, stands for Sub-Password System.
        # Create the six subpasswords
        spw = random.randint(100000, 999999)
        # Make a fullpassword and convert it into bytes
        fpw = (spw + spw + spw + spw + spw + spw)
        fbpw = bytes(fpw)
        try:
            # Open a file an write the fullbytepassword
            with open("fepw", "wb") as fpw_dir:
                fpw_dir.write(fbpw)
            with open("fepw", "rb") as fpw_dir:
                bfpw = fpw_dir.read()
            # Filter out any potential
            # mistakes using brute force. 
            # And yes, i know i could use
            # semicolons to save space, but
            # why bother???
            key = Fernet.generate_key()
            fepw = Fernet(key).encrypt(bfpw)
            key = Fernet.generate_key()
            fe2pw = Fernet(key).encrypt(fepw)
            key = Fernet.generate_key()
            fe3pw = Fernet(key).encrypt(fe2pw)
            key = Fernet.generate_key()
            fe4pw = Fernet(key).encrypt(fe3pw)
            key = Fernet.generate_key()
            fe5pw = Fernet(key).encrypt(fe4pw)
            return fe5pw
        except FileError:
            print("Error: Couldn't find the needed files.")

    def binargs(priarg, 
                secarg,
                triarg, 
                quadarg,) -> int: # Makes a binary-like object out of 4 args.
        # Get the arg methods
        plusarg = priarg + secarg + triarg + quadarg 
        minarg = priarg - secarg - triarg - quadarg
        mularg = priarg * secarg * triarg * quadarg
        # Format the args into binary
        binplusarg = bin(plusarg) 
        binminarg = bin(minarg)
        binmularg = bin(mularg)
        # Make a full argument
        fullarg = binplusarg + binminarg + binmularg
        return fullarg
        
class Html():
    '''
    Base class for ``Html-based`` functions in pyMod.
    the Html class provides an easy way to
    web scrape using the bs4 module!

    For example:

        >>> from pyMod import *
        >>> ht = Html
        >>> ht.web_scraper("https://www.python.org/")
        Welcome to Python.org
        Notice: While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience.
        Skip to content
        ▼ Close
        Python
        PSF
        Docs
        PyPI
        Jobs
        Community
        ▲ The Python Network
        Donate
        ≡ Menu
        Search This Site
        # There's much more, but i wont add them here.
        >>> ht.html_scraper("https://www.python.org/")
        <!doctype html>
        <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
        <!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
        <!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
        <!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->
        <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-TF35YF9CVH"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-TF35YF9CVH');
        </script>
        <!-- Plausible.io analytics -->
        <script defer data-domain="python.org" src="https://plausible.io/js/script.js"></script>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
        <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js">
        <meta name="application-name" content="Python.org">
        <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
        <meta name="apple-mobile-web-app-title" content="Python.org">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black">
        # There's much more, but i won't add them here.
    '''

    if html_error == True:
        raise ModuleError('''The necessary modules needed to use this pyMod class were
unable to be found.''')

    # Note that this web scraper does NOT run fast at all,
    # and doesn't have permission for some sites (Though
    # i think that's just a problem with bs4).
    def web_scraper(url=None): # The web scraper
        if url == None:
            raise VoidError("""
VoidError: no value was inputted, so pyMod
can't read your program. 
                            """)
        else:
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8") # Decode the site
            soup = BeautifulSoup(html, "html.parser") 
            text = (soup.get_text())
            return(text)

    def html_scraper(url=None): # Scrape all code in the website (html code, at least)
        if url == None:
            raise VoidError("""
VoidError: no value was inputted, so pyMod
can't read your program. 
                            """)
        else:
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8") # Decode the site
            return(html)
        
class Compiler():
    '''Base class for compiling in pyMod'''

    def compile_exec(filename, object):
        obj = compile(object, filename, 'exec')
        exec(obj)

def demo():
    '''pyMod demo function'''

    Console.clear()
    print(f'''
                  888b     d888               888 
                  8888b   d8888               888 
                  88888b.d88888               888 
88888b.  888  888 888Y88888P888  .d88b.   .d88888 
888 "88b 888  888 888 Y888P 888 d88""88b d88" 888 
888  888 888  888 888  Y8P  888 888  888 888  888 
888 d88P Y88b 888 888   "   888 Y88..88P Y88b 888 
88888P"   "Y88888 888       888  "Y88P"   "Y88888 
888           888                                 
888      Y8b d88P                                 
888       "Y88P"                                   
             
pyMod ver {__ver__}, made by {__author__}.
Current python version: {__pyver__}''')
    time.sleep(2.5)
    print('''
This is a collection of some modules that i made; decor, 
class_decor and pyLauncher, but i also added some more
features that weren't originally
in any of these modules.
''')
    time.sleep(2.5)
    print('Please take a look at the function and class list below:')
    time.sleep(2.5)
    print('''
:``PluginMod()``:
    :``@register`` - register function as a plugin
    :``log()`` - view all current plugins
:``Pyfiles()``:
    :``create_file(filename)`` - create file
    :``write_file(filename, text)`` - create and write file
    :``read_file(filename)`` - read file, then print out its contents
    :``append_file(filename, text) ``- append file, as in add text to the end
    :``rename_file(filename, new_filename)`` - rename file
    :``delete_file(filename) - delete file``
:``Decor()``:
    :``@do_twice`` - Deprecated function
    :``@timer`` - set a timer
    :``@debug`` - debug a specific function
    :``@slow_down`` - slow down a specific function
    :``@repeat(num_times)`` - repeat a function a set aount of times, leave empty for value 2
    :``@count_calls`` - counts how many times something ha been called
    :``@singleton`` - store function as singleton
    :``@cache`` - hold info
:``Cryptography()``:
    :``encrypt(filename)`` - Encrypts files (Use at your own risk)
    :``decrypt(filename)`` - Decrypts encrypted files
:``Console()``:
    :``printc(text, fg, bg)`` - coloured text, really awesome!
    :``printf(text, fs)`` - fontstyles to your text
    :``printcf(text, fs, fg, bg)`` - text with fontstyles and colours!
    :``clear()`` - clear shell
:``Codecs()``:
    :``rot13_encode(s)`` - encode a string using the rot13 encoding system!
    :``rot13_decode(s)`` - decode a string using the rot13 decoding system!
    :``obfuscator(code)`` - Deprecated function
    :``deobfuscator(code)`` - Deprecated function
    :``spws()`` - Password system, stands for Sub-PassWord System.
    :``binargs()`` - Makes a binary-like object out of 4 arguments.
:``Html()``:
    :``web_scraper(url)`` - Tool that scrapes the web so that you can gather info! Beware though, it's not fast
    :``html_scraper(url)`` - Same as the webscraper, but it scrapes all of the code.
:``Compiler()``:
    :``compile_exec(filename, object)`` - Compiles and executes.''')
    time.sleep(3)
    print('''
Also, please use the "from pyMod import *" function
when importing pyMod. If you don't know, it imports everything
in pyMod, but you dont need to use the "pyMod." prefix to 
access functions. 
''')
    time.sleep(3)
    print('''Some functions in this module may be bugged but thats hopefully okay. We don't need A+ code
here, we need functioning code, which there hopefully is in
this module.
''')
    time.sleep(2.5)
    print('Also, the author of this module isn\'t liable for any, uhh,')
    time.sleep(2)
    print('''crimes commited using this software. 
But asides from that, enjoy!
''')
    
# Keywords to make it easier to get started quickly, e.g:
# from pyMod import _pm
_pm = PluginMod
_pf = Pyfiles
_dc = Decor
_cg = Cryptography
_cs = Console
_cd = Codecs
_hm = Html

# Create a dictionary to hold the simple info in pyMod.
pyModInfo = {
    "Author" : __author__,
    "Pymod version" : __ver__,
    "Python version" : __pyver__,
    "Errors" : __errors__,
    "Warnings" : __warnings__,
}
'''Dictionary to hold all pyMod info'''

# Making a variable to hold ALL of the pyMod namespace,
# if you really wanna pollute the namespace of your 
# project you could probbably use this.
IncludeAll = [
    Locals, __errors__, __warnings__,
    SoftwareVersion, PyModVersion,
    __author__, __ver__, __pyver__,
    PluginMod, Pyfiles, Decor,
    Cryptography, Console,
    Codecs, Html, Compiler, demo,
    pyModInfo,
]

if __name__ == '__main__':

    # Clean up namespace
    del (
    PluginMod, Pyfiles, Decor, Cryptography, 
    Codecs, functools, warnings, encode, decode, urlopen, 
    __errors__, __warnings__, __all__, _pm, _pf, _dc,
    _cg, _cs, _cd, _hm, IncludeAll
    )

    # If this file is run as a script, we play the demo.
    demo()
      
    # Clean up the rest of the namespace.
    del (
        __author__, __ver__, __pyver__,
        demo, Html, sys, time, os, Console,
    )

# End of module. 
