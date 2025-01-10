/*
Supermath module! Since, i uhh; think the math module is way to useless. This
was originally written in python (only included three functions back then), but
since my coding skills have evolved, i have now rewritten and added to it in
Golang. Includes some cool functions, i you wanna, uhh, take a look at them, 
they're here down below:

:factorial - Calculate the factorial of a number, which
means that factorial(n=5) = 5!.

:prime - Calculate if a number is prime or not, returns
this info in the form of a boolean.

:kuan - Knuth's up-arrow notation, don't really have time
to explain, but you can probably search for it on the internet.

:mode - Calculate the calculation... Mode? I don't know what it's called,
but it returns, 1 if number is positive, -1 if number is negative, and
0 if number is 0 (Or any, other weird... Exception nobody has told me
about. :/)

Also, if you're reading this
and not using Neovim; fuck off and 
never return. You have just lost
privileges to this module.

Single-Handedly made by Elis Staaf.
*/

package supermath 

import (
    "fmt"
)

const (
    AUTHOR string = "Elis Stääf"
    VERSION float32 = 0.1
)

// NOTE: The "n" parameter always means "number"
func factorial(n int) int {
    if n == 1 {
	return 1
    }
    return n * factorial(n-1)
}

func prime(n int) bool {
    isPrime := true
    if n == 0 || n == 1 {
        return false
    } else {
        for i := 2;i <= n / 2;i++{
            if n % i == 0 {
                return false
            }
        }
        if isPrime == true {
            return true
	}
    }
}

// To read about this function, visit:
// https://en.wikipedia.org/wiki/Knuth%27s_up-arrow_notation
func kuan(n int, arr int, i int) int {
    if arr == 1 {
	return math.Pow(n, i)
    }
    res = n

    for j:=0;j<=i;j++ {
	res = kuan(n, arrows - 1, res)
    }
    return res
}

func mode(n int) int {
    if n > 0 {
	return 1
    } if n < 0 {
	return -1
    } else {
	return 0
    }
}

// TODO: Try to find a way to generate g64.
