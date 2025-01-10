"""Supermath is a python module based upon 
making better mathematics for python. Since
i'm not the maintainer for the "math" module,
i guess i'll make my own? So yeah, enjoy!
"""

# trycatch import model
try:
    import sys
    import math
    from functools import cache
    from hyperop import hyperop # Dependency
except ImportError:
    print("ImportError: Invalid imports.")
    quit(1)


class SoftwareVersion():
    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = str(major)
        self.minor = str(minor)
        self.patch = str(patch)
    def __str__(self) -> str:
        return ".".join([self.major, self.minor, self.patch])

__version__ = SoftwareVersion(0, 0, 2)
__python__ = ".".join([str(sys.version_info.major), str(sys.version_info.minor)])
__all__ = [
"factorial", "prime", 
"kuan", "g64",
]


def factorial(n) -> int:
    if n == 1:
        return 1
    return n * factorial(n-1)

def prime(n) -> bool:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

# If you're wondering what this is, this
# is something called "Knuth's up-arrow 
# notation" in math.
@cache
def kuan(n, arrows, k) -> int:
    if arrows == 1:
        return n ** k
    res = n

    for i in range(k):
        res = kuan(n, arrows - 1, res)
    return res

# Graham's number (g64)
def g64() -> int:
    # This should TECHNICALLY, given infinite computing power;
    # generate Graham's number (g64).
    g = 4
    for n in range(1,64+1):
        g = hyperop(g+2)(3,3)
    return g


