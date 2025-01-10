

class StructParser:

    def __init__(self, source):
        self.source = source
        self.ext = source.split(".")[-1]
        self.columns = {}
        self.structs = {}

        if self.ext!= "struct":
            raise ValueError("Imvalid file extension. Please provide a STRUCT file.")

        with open(self.source, "r") as source:
            self.lines = source.readlines()
            source.close()

        column = 0
        for line in self.lines:
            self.tokens = line.split(" ")

            self.values = "".join(self.tokens).split(":")
            index = 0

            for value in self.values:
                self.columns[column, index] = value.strip("\n")
                index += 1
            column += 1
    
    def make(self, target):
        self.format = {}
        self.lists = []
        for column, value in self.columns:
            if value not in self.format:
                self.format[value] = [self.columns[column, value]]
                continue
            self.format[value].append(self.columns[column, value])
        for list in self.format:
            self.format[list] = ",".join(self.format[list])
        for list in self.format:
            self.lists.append(self.format[list])
        self.lists = "\n".join(self.lists)
        with open(target, "w") as output:
            output.write(self.lists)
            print(self.lists)

if __name__ == "__main__":
    parser = StructParser("./index.struct")
    parser.getValues()