

class Optimizer:
    def __init__(self):
        pass

    def optimize(self, tac_code):
        optimized_code = []

        for line in tac_code:
            # Split the line into tokens
            tokens = line.split()

            if len(tokens) == 5 and tokens[3] in ('+', '-', '*', '/'):
                # Constant folding
                try:
                    result = eval(f'{tokens[2]} {tokens[3]} {tokens[4]}')
                    optimized_code.append(f'{tokens[0]} = {result}')
                except ValueError:
                    optimized_code.append(line)
            elif len(tokens) == 4 and tokens[2] == '=' and tokens[3].isdigit():
                # Constant propagation
                optimized_code.append(f'{tokens[0]} = {tokens[3]}')
            else:
                # Dead code removal (retain only lines that contribute to the final result)
                if tokens[0].startswith('T') or tokens[0].startswith('return'):
                    optimized_code.append(line)

        return optimized_code


