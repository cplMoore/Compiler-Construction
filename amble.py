

class PreamblePostambleGenerator:
    def __init__(self):
        self.var_offset = 0

    def generate_preamble(self):
        preamble = [
            'PUSH FP',             # Save the old frame pointer
            'MOV FP, SP',          # Set the frame pointer to the current stack pointer
            'SUB SP, SP, <size>',  # Allocate space for local variables
        ]
        return preamble

    def generate_postamble(self):
        postamble = [
            'ADD SP, SP, <size>',  # Deallocate space for local variables
            'POP FP',              # Restore the old frame pointer
            'RET',                 # Return from the function
        ]
        return postamble

    def generate_tac_with_preamble_postamble(self, tac_code):
        breakpoint()
        preamble = self.generate_preamble()
        postamble = self.generate_postamble()

        # Replace '<size>' with the actual size needed for local variables
        size = self.calculate_local_variable_size(tac_code)
        preamble[-1] = preamble[-1].replace('<size>', str(size))
        postamble[0] = postamble[0].replace('<size>', str(size))

        # Combine the preamble, TAC code, and postamble
        full_code = preamble + tac_code + postamble
        return full_code

    def calculate_local_variable_size(self, tac_code):
        # Simple calculation: size = number of temporary variables used in TAC
        temp_vars = set()
        for line in tac_code:
            tokens = line.split()
            for token in tokens:
                if token.startswith('T'):
                    temp_vars.add(token)

        return len(temp_vars)


