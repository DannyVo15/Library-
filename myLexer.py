# myLexer.py
# Author: Danny Vo
# Description:
# This file implements a lexer for arithmetic expressions.
# It tokenizes numbers, operators, parentheses, comments, and whitespace.
# The lexer is used as input to the LabP2 parser to build ASTs.


import re

# Author: [Danny Vo]
# Date: [10/15/1999]
# Time Taken: [4 hours & 26 minutes]
# Your commenting character used for the lexer: #

# Token types
RR_INT = 'RR_INT'
RR_FLOAT = 'RR_FLOAT'
RR_PLUS = 'RR_PLUS'
RR_MINUS = 'RR_MINUS'
RR_MUL = 'RR_MUL'
RR_DIV = 'RR_DIV'
RR_LPAREN = 'RR_LPAREN'
RR_RPAREN = 'RR_RPAREN'
RR_COMMENT = 'RR_COMMENT'
RR_ILLEGAL = 'RR_ILLEGAL'

# Create a Token Class with position tracking
class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None, line=None, column=None):
        self.type = type_
        self.value = value
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, pos_start={self.pos_start}, pos_end={self.pos_end}, line={self.line}, column={self.column})"

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = -1
        self.current_char = None
        self.line = 1
        self.column = -1
        self.advance()

    def advance(self):
        self.pos += 1
        self.column += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
            if self.current_char == '\n':
                self.line += 1
                self.column = -1
        else:
            self.current_char = None

    def make_tokens(self):
        tokens = []
        patterns = [
            (r'\d+(\.\d+)?', lambda match, pos, line, column: Token(
                RR_FLOAT if '.' in match.group(0) else RR_INT,
                float(match.group(0)) if '.' in match.group(0) else int(match.group(0)),
                pos_start=pos, pos_end=pos + len(match.group(0)), line=line, column=column)),
            (r'\+', lambda match, pos, line, column: Token(RR_PLUS, '+', pos_start=pos, pos_end=pos + 1, line=line, column=column)),
            (r'-', lambda match, pos, line, column: Token(RR_MINUS, '-', pos_start=pos, pos_end=pos + 1, line=line, column=column)),
            (r'\*', lambda match, pos, line, column: Token(RR_MUL, '*', pos_start=pos, pos_end=pos + 1, line=line, column=column)),
            (r'/', lambda match, pos, line, column: Token(RR_DIV, '/', pos_start=pos, pos_end=pos + 1, line=line, column=column)),
            (r'\(', lambda match, pos, line, column: Token(RR_LPAREN, '(', pos_start=pos, pos_end=pos + 1, line=line, column=column)),
            (r'\)', lambda match, pos, line, column: Token(RR_RPAREN, ')', pos_start=pos, pos_end=pos + 1, line=line, column=column)),
            (r'#[^\n]*', lambda match, pos, line, column: None),  # Comment
            (r'\s+', lambda match, pos, line, column: None),      # Whitespace
        ]

        while self.current_char is not None:
            matched = False
            for pattern, action in patterns:
                match = re.match(pattern, self.text[self.pos:])
                if match:
                    token = action(match, self.pos, self.line, self.column)
                    self.pos += len(match.group(0))
                    self.column += len(match.group(0))
                    self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                    if token:
                        tokens.append(token)
                    matched = True
                    break
            if not matched:
                tokens.append(Token(
                    RR_ILLEGAL,
                    value=self.current_char,
                    pos_start=self.pos,
                    pos_end=self.pos + 1,
                    line=self.line,
                    column=self.column
                ))
                self.advance()
        return tokens

    def skip_comment(self):
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

# Function to execute lexer
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens = lexer.make_tokens()
    return tokens
