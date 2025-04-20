from myLexer import run as lexer_run
from LabP2 import Parser, Token

while True:
    try:
        text = input("R@R: ")
        if text.strip().lower() in {"exit", "quit"}:
            break
        if text.strip() == "":
            continue

        # Run the lexer
        tokens = lexer_run("<stdin>", text)

        # Print formatted tokens
        print("\nTokens:")
        formatted = [f"{t.type.split('_')[-1]}({t.value})" for t in tokens]
        print(f"[{', '.join(formatted)}]")

        # Add EOF token
        tokens.append(Token(Token.EOF, None))

        # Run the parser
        parser = Parser(tokens)
        ast = parser.expression()

        # Print AST
        print("\nAbstract Syntax Tree (AST):")
        print(ast)

    except Exception as e:
        print("\nParsing Error: Syntax Error:", e)




# ================================
# Test Cases 
# ================================

# Expression: -5
# Tokens: [MINUS(-), INT(5)]
# AST: BinOp '-' (0 - 5)

# Expression: 1 + 2
# Tokens: [INT(1), PLUS(+), INT(2)]
# AST: BinOp '+' with Num(1) and Num(2)

# Expression: 4 - 3
# Expression: 6 * 7
# Expression: 8 / 2
# → All basic arithmetic ops work and show correct ASTs

# Expression: 4 * 2 - 6
# → Operator precedence: MUL before MINUS

# Expression: ((2 + 3)) * ((4))
# → Nested parentheses work

# Expression: 3.14 + 2
# Expression: 6.5 * 2
# → Floats supported

# Expression: -(2 + 3)
# Expression: -(-4)
# Expression: -(1 + 2 * 3)
# → Unary minus works, including nested and complex expressions

# Expression: 3 +
# → Error: Invalid factor (missing right operand)

# Expression: (4 + 5
# → Error: Expected ')' (unclosed parenthesis)
