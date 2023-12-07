
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
        self.visit(ast)
        return self.code

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        #Checks the method name and calls the appropriate method
        #Got help with chatgpt on the if else statements
        if method_name == 'visit_tuple':
            return self.visit_tuple(node)
            
        if method_name == 'visit_int':
            return self.visit_int(node)
            
        if method_name == 'visit_str':
            return self.visit_str(node)
            
        # Return error if no matches
        else:
            return self.generic_visit(node)

    def visit_tuple(self, node):
        if isinstance(node, tuple):
        
            root = node[0]
            if root == 'main':
                self.code.append(f'{root}')
                self.visit(node[1])
                self.visit(node[2])
                
            if root in ('+', '-', '*', '/'):
                temp_result = self.new_temp()
                self.code.append(f'{temp_result} = {self.visit(node[1])} {root} {self.visit(node[2])}')
                return temp_result
                
            if root == '=':
                self.code.append(f'{node[1]} = {self.visit(node[2])}')
                
            if root == '(':
                return self.visit(node[1])
                
            if root == 'return':
                self.code.append(f'return {self.visit(node[1])}')
    
    def visit_int(self, node):
        if isinstance(node, tuple):
            return self.code.append(node)

        # If it's a leaf node, return its number value
        return node
        
    def visit_str(self, node):
        if isinstance(node, tuple):
            return self.code.append(node)

        # If it's a leaf node, return its ID value
        return node        

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
