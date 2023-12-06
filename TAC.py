
class TACGenerator:
    
    def __init__(self):
        self.code = []  # To store the generated TAC
        self.temp_count = 0  # Counter for generating temporary variables
        self.block_count = 0 # A way to keep up with basic block statements

    def new_temp(self):
        temp_var = f'T{self.temp_count}'
        self.temp_count += 1
        return temp_var

    def generate_tac(self, ast):
        breakpoint()
        
        self.temp_count = 0  # Reset the temporary variable counter
        self.visit(ast)
        return self.code

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        #Checks the method name and calls the appropriate method
        #Got help with chatgpt on the if else statements
        if method_name == 'visit_program':
            return self.visit_program(node)
        if method_name == 'visit_stmt_list':
            return self.visit_stmt_list(node)
        if method_name == 'visit_stmt':
            return self.visit_stmt(node)
        if method_name == 'visit_tuple':
            return self.visit_tuple(node)
        if method_name == 'visit_int':
            return self.visit_int(node)
        if method_name == 'visit_return_stmt':
            return self.visit_return_stmt(node)
        # Return error if no matches
        else:
            return self.generic_visit(node)

    def visit_program(self, node):
        if isinstance(node, tuple):
            main_label = f'{node[0]}:'
            self.code.append(main_label)
            self.visit(node[1])  # Visit stmt_list
            self.visit(node[2])  # Visit return_stmt

    def visit_stmt_list(self, node):
        if isinstance(node, tuple):
            for stmt in node:
                self.visit(stmt)

    def visit_stmt(self, node):
        if isinstance(node, tuple):
            if node[0] == '=':
                self.code.append(f'{node[1]} = {self.visit(node[2])}')
            if node[0] == '(':
                return self.visit(node[1])
            

    def visit_tuple(self, node):
        if isinstance(node, tuple):
            root = node[0]
            left = node[1]
            right = node[2]
            if root == 'main':
                self.code.append(f'{node[0]} {self.visit(left)} {self.visit(right)}')
            if root in ('+', '-', '*', '/'):
                temp_result = self.new_temp()
                self.code.append(f'{temp_result} = {self.visit(left)} {root} {self.visit(right)}')
                return temp_result
    
    def visit_int(self, node):
        if isinstance(node, tuple):
            return self.code.append(node)

        # If it's a leaf node, return its number value
        return node
                
    def visit_return_stmt(self, node):
        return_stmt = f'return {self.visit(node[1])}'
        self.code.append(return_stmt)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
