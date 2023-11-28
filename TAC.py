class TACGenerator:
    def __init__(self):
        self.code = []  # To store the generated TAC
        self.temp_count = 0  # Counter for generating temporary variables

    def new_temp(self):
        temp_var = f'T{self.temp_count}'
        self.temp_count += 1
        return temp_var

    def generate_tac(self, ast):
        self.code = []  # Reset the code
        self.temp_count = 0  # Reset the temporary variable counter
        self.visit(ast)
        return self.code

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_program(self, node):
        main_label = f'{node[0]}:'
        self.code.append(main_label)
        self.visit(node[1])  # Visit stmt_list
        self.visit(node[2])  # Visit return_stmt

    def visit_stmt_list(self, node):
        for stmt in node:
            self.visit(stmt)

    def visit_stmt(self, node):
        if isinstance(node, tuple):
            if node[0] == '=':
                self.code.append(f'{node[1]} = {self.visit(node[2])}')
            elif node[0] == '(':
                return self.visit(node[1])

    def visit_expr(self, node):
        if isinstance(node, tuple):
            op, left, right = node
            if op in ('+', '-', '*', '/'):
                temp_result = self.new_temp()
                self.code.append(f'{temp_result} = {self.visit(left)} {op} {self.visit(right)}')
                return temp_result

    def visit_factor(self, node):
        if isinstance(node, tuple):
            return self.visit(node[1])  # Return the ID or NUM

        # If it's a leaf node, return its value (ID or NUM)
        return node

    def visit_return_stmt(self, node):
        return_stmt = f'return {self.visit(node[1])}'
        self.code.append(return_stmt)


if __name__ == '__main__':
    from compiler import MyParser

    # Example usage
    parser = MyParser()
    code = '''
    INT MAIN LPAREN RPAREN LCB
        INT x ASSIGN 5 SEMI
        INT y ASSIGN 10 SEMI
        RETURN x + y SEMI
    RCB
    '''
    tokens = parser.tokenize(code)
    ast = parser.parse(tokens)
    
    tac_generator = TACGenerator()
    tac_code = tac_generator.generate_tac(ast)

    for line in tac_code:
        print(line)
