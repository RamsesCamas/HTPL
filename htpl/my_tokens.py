from enum import Enum, auto, unique
from typing import Dict, NamedTuple


class TokenType(Enum):
    ASSIGN = auto()
    BOOL = auto()
    COMMA = auto()
    DATATYPE = auto()
    DOT = auto()
    EQUAL = auto()
    EOF = auto()
    FALSE = auto()
    #FLOAT = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INPUT = auto()
    INT = auto()
    LARROW = auto()
    LANGNAME = auto()
    LBRACE = auto()
    LPAREN = auto()
    MS = auto()
    NAME = auto()
    PLUS =  auto()
    PRINT = auto()
    QUOTE = auto()
    RARROW = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    SLASH = auto()
    #STRING = auto()
    TRUE = auto()
    TYPE = auto()
    VAR = auto()


class Token(NamedTuple):
    token_type : TokenType
    literal:str
    
    def __str__(self) -> str:
        return f'Type: {self.token_type} \t Valor: {self.literal}'

def lookup_token_type(literal:str) -> TokenType:
    keywords: Dict[str,TokenType] = {
        'var': TokenType.VAR,
        'type': TokenType.TYPE,
        'integer': TokenType.DATATYPE,
        'name': TokenType.NAME,
        'float': TokenType.DATATYPE,
        'True': TokenType.TRUE,
        'False': TokenType.FALSE,
        'print': TokenType.PRINT,
        'input': TokenType.INPUT,
        'assign': TokenType.ASSIGN,
        'HTPL': TokenType.LANGNAME,
    }

    return keywords.get(literal, TokenType.IDENT)