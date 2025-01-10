/*
== Mathem; glorified calculator ==

Mathem is a glorified calculator/programming
language that I made in my free time. It's
pretty cool, but pretty useless. Enjoy!

Single-handedly made by Elis Staaf.
*/
package main

import (
    "bufio"
    "fmt"
    "math"
    "os"
    "strconv"
    "strings"
    "unicode"
)

// Token types
const (
    AUTHOR      = "Elis Staaf"
    EOF         = iota
    NUMBER      // individual numbers
    PLUS        // +
    MINUS       // -
    MULT        // *
    DIV         // /
    LPAREN      // (
    RPAREN      // )
    IDENTIFIER   = iota + 100 // Identifier token (for variable names)
    ASSIGN                   // Assignment token (=)
    FUNCTION                 // Function call token
)

// Token structure
type Token struct {
    Type  int
    Value string
}

// Lexer struct
type Lexer struct {
    input string
    pos   int
}

// NewLexer creates a new lexer
func NewLexer(input string) *Lexer {
    return &Lexer{input: input, pos: 0}
}

// NextToken retrieves the next token from the input
func (l *Lexer) NextToken() Token {
    for l.pos < len(l.input) {
        switch l.input[l.pos] {
        case ' ':
            l.pos++
        case '+':
            l.pos++
            return Token{Type: PLUS, Value: "+"}
        case '-':
            l.pos++
            return Token{Type: MINUS, Value: "-"}
        case '*':
            l.pos++
            return Token{Type: MULT, Value: "*"}
        case '/':
            l.pos++
            return Token{Type: DIV, Value: "/"}
        case '(':
            l.pos++
            return Token{Type: LPAREN, Value: "("}
        case ')':
            l.pos++
            return Token{Type: RPAREN, Value: ")"}
        case '=':
            l.pos++
            return Token{Type: ASSIGN, Value: "="}
        default:
            if unicode.IsDigit(rune(l.input[l.pos])) {
                start := l.pos
                for l.pos < len(l.input) && unicode.IsDigit(rune(l.input[l.pos])) {
                    l.pos++
                }
                return Token{Type: NUMBER, Value: l.input[start:l.pos]}
            } else if unicode.IsLetter(rune(l.input[l.pos])) {
                start := l.pos
                for l.pos < len(l.input) && (unicode.IsLetter(rune(l.input[l.pos])) || unicode.IsDigit(rune(l.input[l.pos]))) {
                    l.pos++
                }
                // Check if token is a function like "max", "min"
                ident := l.input[start:l.pos]
                switch ident {
                case "max", "min", "sqrt", "pow":
                    return Token{Type: FUNCTION, Value: ident}
                }
                return Token{Type: IDENTIFIER, Value: ident}
            }
            l.pos++
        }
    }
    return Token{Type: EOF, Value: ""}
}

// Parser struct
type Parser struct {
    lexer   *Lexer
    current Token
}

// NewParser creates a new parser
func NewParser(lexer *Lexer) *Parser {
    parser := &Parser{lexer: lexer}
    parser.nextToken() // Initialize the first token
    return parser
}

// nextToken updates the current token
func (p *Parser) nextToken() {
    p.current = p.lexer.NextToken()
}

// VariableMap holds variable names and their values
type VariableMap map[string]float64

var variables VariableMap = make(VariableMap)

// ParseExpression parses an expression
func (p *Parser) ParseExpression() float64 {
    // We attempt to read variable assignments first
    if p.current.Type == IDENTIFIER {
        variableName := p.current.Value
        p.nextToken() // move past the identifier

        if p.current.Type == ASSIGN {
            p.nextToken() // move past the '='
            value := p.ParseExpression() // evaluate the right-hand side
            variables[variableName] = value // store in variables
            return value
        } else {
            // If it's just an identifier with no assignment, retrieve its value
            return variables[variableName]
        }
    }

    result := p.ParseTerm()
    for p.current.Type == PLUS || p.current.Type == MINUS {
        token := p.current
        p.nextToken()
        if token.Type == PLUS {
            result += p.ParseTerm()
        } else if token.Type == MINUS {
            result -= p.ParseTerm()
        }
    }

    return result
}

// ParseTerm parses a term (handles multiplication and division)
func (p *Parser) ParseTerm() float64 {
    result := p.ParseFactor()

    for p.current.Type == MULT || p.current.Type == DIV {
        token := p.current
        p.nextToken()
        if token.Type == MULT {
            result *= p.ParseFactor()
        } else if token.Type == DIV {
            result /= p.ParseFactor()
        }
    }

    return result
}

// ParseFactor parses a single factor (number, parenthesis, or function call)
func (p *Parser) ParseFactor() float64 {
    token := p.current

    if token.Type == NUMBER {
        value, _ := strconv.ParseFloat(token.Value, 64)
        p.nextToken()
        return value
    } else if token.Type == IDENTIFIER {
        varName := token.Value
        p.nextToken()
        return variables[varName] // return variable value
    } else if token.Type == LPAREN {
        p.nextToken()
        result := p.ParseExpression()
        if p.current.Type == RPAREN {
            p.nextToken() // Consume ')'
        }
        return result
    } else if token.Type == FUNCTION { // Function handling
        functionName := token.Value
        p.nextToken() // move past function
        p.nextToken() // move to '('
        arg := p.ParseExpression() // get argument

        switch functionName {
        case "max":
            p.nextToken() // move past the comma (or you can handle it differently)
            arg2 := p.ParseExpression() // get second argument
            return math.Max(arg, arg2)
        case "min":
            p.nextToken() // move past the comma
            arg2 := p.ParseExpression() // get second argument
            return math.Min(arg, arg2)
        case "sqrt":
            return math.Sqrt(arg)
        case "pow":
            p.nextToken() // move past the comma
            arg2 := p.ParseExpression() // get second argument
            return math.Pow(arg, arg2)
        }
    }

    return 0
}

// Eval evaluates a mathematical expression from its string representation
func Eval(input string) float64 {
    lexer := NewLexer(strings.TrimSpace(input))
    parser := NewParser(lexer)
    return parser.ParseExpression()
}

// GetUserInput gets mathematical expressions from the user
func GetUserInput() {
    scanner := bufio.NewScanner(os.Stdin)

    for {
        fmt.Print("> ")
        scanner.Scan()
        input := scanner.Text()
        if input == "end" {
            break
        }
        result := Eval(input)
        fmt.Printf("%f\n", result)
    }
}

func main() {
    fmt.Println("Welcome to Mathem, a simple programming language!")
    fmt.Println("Type 'end' to exit.")
    GetUserInput()
}
