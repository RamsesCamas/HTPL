from unittest import TestCase
from typing import List

from htpl.my_tokens import(
    Token,
    TokenType
)

from htpl.lexer import Lexer

class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@'),
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_one_character_operator(self) -> None:
        source: str = '=+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.EQUAL, '='),
            Token(TokenType.PLUS, '+'),
        ]

        self.assertEqual(tokens, expected_tokens)


    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_delimiters(self) -> None:
        source = '<>(){},;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LARROW, '<'),
            Token(TokenType.RARROW, '>'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_assignment(self) -> None:
        source: str = '<var type="integer" name="my_int1">  25 </var>'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(18):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LARROW, '<'),
            Token(TokenType.VAR, 'var'),
            Token(TokenType.TYPE, 'type'),
            Token(TokenType.EQUAL, '='),
            Token(TokenType.QUOTE, '"'),
            Token(TokenType.DATATYPE, 'integer'),
            Token(TokenType.QUOTE, '"'),
            Token(TokenType.NAME, 'name'),
            Token(TokenType.EQUAL, '='),
            Token(TokenType.QUOTE, '"'),
            Token(TokenType.IDENT, 'my_int1'),
            Token(TokenType.QUOTE, '"'),
            Token(TokenType.RARROW, '>'),
            Token(TokenType.INT, '25'),
            Token(TokenType.LARROW, '<'),
            Token(TokenType.SLASH, '/'),
            Token(TokenType.VAR, 'var'),
            Token(TokenType.RARROW, '>'),
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_print_variables(self) -> None:
        source: str = '<print> Me llamo ${my_string} y tengo ${my_int} años. </print>'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(21):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LARROW, '<'),
            Token(TokenType.PRINT, 'print'),
            Token(TokenType.RARROW, '>'),
            Token(TokenType.IDENT, 'Me'), 
            Token(TokenType.IDENT, 'llamo'), 
            Token(TokenType.MS, '$'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'my_string'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.IDENT, 'y'), 
            Token(TokenType.IDENT, 'tengo'), 
            Token(TokenType.MS, '$'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'my_int'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.IDENT, 'años'), 
            Token(TokenType.DOT, '.'), 
            Token(TokenType.LARROW, '<'),
            Token(TokenType.SLASH, '/'),
            Token(TokenType.PRINT, 'print'),
            Token(TokenType.RARROW, '>'),
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_input(self) -> None:
        source: str = '<input assign="my_input">'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(21):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LARROW, '<'),
            Token(TokenType.INPUT, 'input'),
            Token(TokenType.ASSIGN, 'assign'),
            Token(TokenType.EQUAL, '='),
            Token(TokenType.QUOTE, '"'),
            Token(TokenType.IDENT, 'my_input'),
            Token(TokenType.QUOTE, '"'),
            Token(TokenType.RARROW, '>'),
        ]