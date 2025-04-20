# LabP2.py
# Author: Danny Vo
# Description:
# This program parses arithmetic expressions using a recursive descent parser.
# It supports integers, floating-point numbers, parentheses, and unary operators 
# It builds and prints an Abstract Syntax Tree (AST) for the given input.



class Token:
    INTEGER, FLOAT, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
        'RR_INT', 'RR_FLOAT', 'RR_PLUS', 'RR_MINUS', 'RR_MUL', 'RR_DIV', 'RR_LPAREN', 'RR_RPAREN', 'EOF'
    )

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class NumberNode:
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __repr__(self, level=0):
        indent = "  " * level
        return f"{indent}Num({self.value})"


class BiOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self, level=0):
        indent = "  " * level
        result = f"{indent}BinOp '{self.op.value}'\n"
        result += f"{indent}  Left:\n{self.left.__repr__(level + 2)}\n"
        result += f"{indent}  Right:\n{self.right.__repr__(level + 2)}"
        return result


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def consume_token(self, token_type):
        if self.current_token.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current_token = self.tokens[self.pos]
            else:
                self.current_token = Token(Token.EOF, None)
        else:
            raise Exception(f"Unexpected token {self.current_token.type}, expected {token_type}")

    def factor(self):
        """
        Handles:
        - Numbers (integers and floats)
        - Parenthesis expressions: (expr)
        - Unary minus: -expr
        """
        token = self.current_token

        # Handle numbers
        if token.type == Token.INTEGER or token.type == Token.FLOAT:
            self.consume_token(token.type)
            return NumberNode(token)

        # Handle parenthesis expressions
        elif token.type == Token.LPAREN:
            self.consume_token(Token.LPAREN)
            node = self.expression()
            if self.current_token.type != Token.RPAREN:
                raise Exception("Expected ')'")
            self.consume_token(Token.RPAREN)
            return node

        # Handle unary minus: -expr becomes 0 - expr
        elif token.type == Token.MINUS:
            self.consume_token(Token.MINUS)
            factor_node = self.factor()
            zero_token = Token(Token.INTEGER, 0)
            return BiOpNode(NumberNode(zero_token), Token(Token.MINUS, '-'), factor_node)

        else:
            raise Exception(f"Invalid factor: {token}")

    def term(self):
        left = self.factor()
        while self.current_token.type in (Token.MUL, Token.DIV):
            op_token = self.current_token
            self.consume_token(op_token.type)
            right = self.factor()
            left = BiOpNode(left, op_token, right)
        return left

    def expression(self):
        left = self.term()
        while self.current_token.type in (Token.PLUS, Token.MINUS):
            op_token = self.current_token
            self.consume_token(op_token.type)
            right = self.term()
            left = BiOpNode(left, op_token, right)
        return left


# ======== TEST CASES (Commented Out) ======== #
# tokens1 = [
#     Token(Token.INTEGER, 4),
#     Token(Token.PLUS, "+"),
#     Token(Token.INTEGER, 5),
#     Token(Token.MUL, "*"),
#     Token(Token.INTEGER, 6),
#     Token(Token.MINUS, "-"),
#     Token(Token.INTEGER, 7),
#     Token(Token.EOF, None)
# ]

# parser1 = Parser(tokens1)
# ast1 = parser1.expression()
# print("\nAbstract Syntax Tree (AST) for '4 + 5 * 6 - 7':")
# print(ast1)

# tokens2 = [
#     Token(Token.INTEGER, 4),
#     Token(Token.MUL, "*"),
#     Token(Token.INTEGER, 5),
#     Token(Token.PLUS, "+"),
#     Token(Token.INTEGER, 6),
#     Token(Token.MINUS, "-"),
#     Token(Token.INTEGER, 7),
#     Token(Token.EOF, None)
# ]

# parser2 = Parser(tokens2)
# ast2 = parser2.expression()
# print("\nAbstract Syntax Tree (AST) for '4 * 5 + 6 - 7':")
# print(ast2)
