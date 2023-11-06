# Produces three address code for COMP 5210 compiler construction project.
# Author: Jacob Moore
# Author: Ben Hulsey

# https://stackoverflow.com/questions/62983856/in-lr-parsing-is-it-possible-to-construct-a-non-binary-ast
# Used stackoverflow to walk through AST uses with SLY to get a AST and TAC built

class TAC():

    def generate_3_address_code(self, ast):  
        ir = []
                    
        if ast: 
            if isinstance(ast, tuple):
                if ast[0] in ['Function Definition', 'Variable Assignment', 'Return Statement']:
                    ir.append((ast[1], ':', ast[2]))
                    ir.extend(self.generate_3_address_code(ast[2]))
                else:
                    ir.append((ast[1], '=', ast[2]))
                    ir.extend(self.generate_3_address_code(ast[1]))
                    ir.extend(self.generate_3_address_code(ast[2]))
            elif isinstance(ast, int):
                ir.append(ast)

        return ir
        print(ast)

    def is_jump_instruction(self, instruction):
        return instruction[0] in ("IF", "GOTO")

    def get_jump_target(self, instruction):
        if instruction[0] == "IF":
            return instruction[2]
        elif instruction[0] == "GOTO":
            return instruction[1]
        return None                
     
    # Had ChatGPT help me (JM) create basic blocks for the 3 address code.           
    def generate_basic_blocks(self, instructions):
         leaders = set()
         leader = 0
         leaders.add(leader)
         
         for i, _ in enumerate(instructions):
            if i < len(instructions) - 1 and self.is_jump_instruction(instructions[i]):
                target = self.get_jump_target(instructions[i])
                leaders.add(target)
         if i + 1 < len(instructions):
            leaders.add(i + 1)
         
         # Ensure the last instruction is also a leader
         if not self.is_jump_instruction(instructions[-1]):
            leaders.add(len(instructions))

         basic_blocks = []

         for i in range(len(leaders) - 1):
            start = leaders[i]
            end = leaders[i + 1]
            basic_block = instructions[start:end]
            basic_blocks.append(basic_block)

         return basic_blocks 
