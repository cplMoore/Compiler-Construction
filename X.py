

class X86CodeGenerator:
    def __init__(self):
        self.register_count = 0

    def get_new_register(self):
        register = f'REG{self.register_count}'
        self.register_count += 1
        return register

    def generate_x86_code(self, tac_code):
        x86_code = []

        for line in tac_code:
            tokens = line.split()

            if len(tokens) == 5 and tokens[3] in ('+', '-', '*', '/'):
                # Arithmetic operation
                dest = tokens[0]
                op = tokens[3]
                src1 = tokens[2]
                src2 = tokens[4]

                x86_code.append(f'MOV {dest}, {src1}')
                x86_code.append(f'{op} {dest}, {src2}')
            elif len(tokens) == 4 and tokens[2] == '=':
                # Assignment
                dest = tokens[0]
                src = tokens[3]
                x86_code.append(f'MOV {dest}, {src}')
            elif len(tokens) == 2 and tokens[0].startswith('return'):
                # Return statement
                src = tokens[1]
                x86_code.append(f'MOV EAX, {src}')
                x86_code.append('POP EBX')  # Restore the old frame pointer
                x86_code.append('ADD ESP, <size>')  # Deallocate space for local variables
                x86_code.append('POP EBP')  # Restore the stack pointer
                x86_code.append('RET')  # Return

        return x86_code

    def generate_x86_code_with_preamble_postamble(self, tac_code):
        pp_generator = PreamblePostambleGenerator()
        full_code = pp_generator.generate_tac_with_preamble_postamble(tac_code)
        x86_code = self.generate_x86_code(full_code)
        return x86_code
