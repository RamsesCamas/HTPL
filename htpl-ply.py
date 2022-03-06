import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'VAR',
    'TYPE',
    'NAME',
    'LARROW',
    'EQUAL',
    'QUOTE',
    'RARROW',
    'SLASH',
    'DATATYPE',
    'IDENT',
    'CONTENT',
    'INPUT',
    'ASSIGN',
    'PRINT',
    'DOLLAR',
    'LBRACE',
    'RBRACE'
]

t_VAR = 'var'
t_TYPE = 'type'
t_NAME = 'name'
t_LARROW = '\<'
t_EQUAL = '\='
t_QUOTE = '\"'
t_RARROW = '\>'
t_SLASH = '\/'
t_ignore = ' '
t_DATATYPE = r'integer|float|boolean|string'
t_IDENT = r'(?<=name=").*(?=")'
t_CONTENT = r'(?<=>).*(?=<)'
t_INPUT= r'input'
t_ASSIGN = r'assign'
t_PRINT = r'print'
t_DOLLAR = r'\$'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

def t_error(t):
   print(f"Token inválido: {t.value[0]} {t.lexpos}")
   t.lexer.skip(1)

lexer = lex.lex()

def p_start(p):
    'entrada : expresion'

def p_variable(p):
    'expresion : LARROW VAR TYPE EQUAL QUOTE DATATYPE QUOTE NAME EQUAL QUOTE IDENT QUOTE RARROW CONTENT LARROW SLASH VAR RARROW'
    print("Es válido")
    pass

def p_input(p):
    'expresion : LARROW INPUT ASSIGN EQUAL QUOTE IDENT QUOTE RARROW'
    print("Es válido")
    pass

def p_print(p):
    'expresion : LARROW PRINT RARROW CONTENT LARROW SLASH PRINT RARROW'
    print("Es válido")
    pass

def p_print_v(p):
    'expresion : LARROW PRINT RARROW print-v LARROW SLASH PRINT RARROW'
    print("Es válido")
    pass

def p_print_var(p):
    'print-v : DOLLAR LBRACE IDENT RBRACE'
    print("Es válido")
    pass


def p_error(p):
    error = f"Error de sintáxis en el carácter número: {p.lexpos+1}."
    print(error)

parser = yacc.yacc()

if __name__=='__main__':
    comando = '<print>Me llamo ${my_string} y tengo ${my_int} años. </print>'

    parser.parse(comando)
    lexer.input(comando)