
#~ This is the MochaScript source code.
#~ Feel free to use it for any purpose.
#~ It is open-source and free to modify and distribute.
#~ Thank you for using MochaScript!

#& MochaParser class to parse and execute the MochaScript code.
class MochaParser:

    def __init__(self, file) -> None:
        self.file = file
        self.extension = file.split(".")[-1]
        if self.extension != "ms":
            print("Invalid file extension; please use an MochaScript file (.ms)!")
            exit(1)
        self.file = open(self.file, 'r')
        self.lines = self.file.readlines()
        
        self.types = ["str", "int", "float", "bool"]
        self.vars = {}
        self.funcs = {}

        self.parse_lines()
        
    def parse_lines(self):
        current_func = None
        
        for line in self.lines:
            line = line.strip()  # Remove leading and trailing whitespace
            if line == "" or line.startswith("//"):
                continue

            tokens = line.split(" ")
            token = tokens[0]

            if token == "print":
                self.handle_print(tokens)

            elif token == ":":
                self.handle_output(tokens)

            elif token in self.types:
                self.handle_var_declaration(tokens, token)

            elif token == "fun":
                current_func = self.handle_function_definition(tokens)

            elif current_func is not None:
                self.handle_function_body(line, current_func)

            elif token in self.funcs:
                self.handle_function_call(token, tokens)

    def handle_print(self, tokens):
        string = " ".join(tokens[1:])
        if string in self.vars:
            print(self.vars[string], end="")
        else:
            print(string, end="")

    def handle_output(self, tokens):
        string = " ".join(tokens[1:])
        if string in self.vars:
            print(self.vars[string], end="")
        else:
            print(string, end="")

    def handle_var_declaration(self, tokens, var_type):
        name = tokens[1]
        arrow = tokens[2]
        if arrow != "<=":
            print("SyntaxError: Missing arrow in variable declaration.")
            return
        
        # Join the remaining tokens for the value
        value = " ".join(tokens[3:]).strip()
        
        # Ensure string values are properly quoted if they are strings
        if var_type == "str":
            # Remove surrounding quotes if present, then add them back
            if value.startswith('"') and value.endswith('"'):
                self.vars[name] = value
            else:
                value = f'"{value}"'
                self.vars[name] = value
        else:
            self.vars[name] = self.cast_type(var_type, value)

    def cast_type(self, var_type, value):
        if var_type == "int":
            return int(value)
        elif var_type == "float":
            return float(value)
        elif var_type == "bool":
            return value.lower() == "true"
        else:  # Assume it is a string
            return value.strip('"')

    def handle_function_definition(self, tokens):
        func_name = tokens[1]
        self.funcs[func_name] = []
        return func_name

    def handle_function_body(self, line, func_name):
        if line.startswith("end"):
            return None
        self.funcs[func_name].append(line.strip())

    def handle_function_call(self, func_name, tokens):
        if func_name in self.funcs:
            for func_line in self.funcs[func_name]:
                self.execute_line(func_line)

    def execute_line(self, line):
        tokens = line.split(" ")
        # Handle function calls inside function bodies
        if tokens[0] == "print":
            self.handle_print(tokens)
        elif tokens[0] in self.types:
            self.handle_var_declaration(tokens, tokens[0])
        elif tokens[0] == "python":
            code = " ".join(tokens).replace("python ", "")
            exec(code)

def runScript():
    parse = MochaParser
    while True:
        print("")
        file = input("> ")
        if file == "exit":
            break
        parse(file)
        print("\n")

if __name__ == "__main__":
    runScript()