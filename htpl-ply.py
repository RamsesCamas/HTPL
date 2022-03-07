import ply.lex as lex
import ply.yacc as yacc
import re
from tkinter import Entry, Tk, Label, Button, font

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
    'RBRACE',
    'INPUTVAR',
    'LANGNAME'
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
t_INPUTVAR = r'(?<=assign=").*(?=")'
t_CONTENT = r'(?<=>).*(?=<)'
t_INPUT= r'input'
t_ASSIGN = r'assign'
t_PRINT = r'print'
t_DOLLAR = r'\$'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LANGNAME = r'HTPL'

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

def t_error(t):
   print(f"Token inválido: {t.value[0]} {t.lexpos}")
   t.lexer.skip(1)

lexer = lex.lex()

def change_text(error=False, error_msg=''):
    res_label['text'] = 'Es válido'
    res_label['fg'] = '#46BE51'
    if error:
        res_label['text'] = error_msg
        res_label['fg'] = '#FF0000'

def p_start(p):
    'entrada : expresion'

def p_variable(p):
    'expresion : LARROW VAR TYPE EQUAL QUOTE DATATYPE QUOTE NAME EQUAL QUOTE IDENT QUOTE RARROW CONTENT LARROW SLASH VAR RARROW'
    change_text()
    pass

def p_input(p):
    #<input assign=“hola”>
    'expresion : LARROW INPUT ASSIGN EQUAL QUOTE INPUTVAR QUOTE RARROW'
    change_text()
    pass

def p_print(p):
    'expresion : LARROW PRINT RARROW CONTENT LARROW SLASH PRINT RARROW'
    change_text()
    pass

def p_print_v(p):
    'expresion : LARROW PRINT RARROW print-v LARROW SLASH PRINT RARROW'
    change_text()
    pass

def p_print_var(p):
    'print-v : DOLLAR LBRACE IDENT RBRACE'
    change_text()
    pass


def p_error(p):
    error = 'Token(s) inválidos'
    if p is not None:
        error = f"Error de sintáxis en el carácter número: {p.lexpos+1}."
    change_text(True,error_msg=error)

parser = yacc.yacc()

def execute_lexer_and_parser():
    entrada = entry_command.get()
    formated_entry = re.sub('> +(?=[\w]*)','>',entrada)

    parser.parse(formated_entry)
    lexer.input(formated_entry)


if __name__=='__main__':
    root = Tk()
    root.title('Lexer y Parser HTPL')
    root.geometry('800x200')
    my_font = font.Font(size=15)

    entry_command = Entry(root,width=50,font=my_font)
    entry_command.place(x=0,y=80)

    btn_analizar = Button(root, text='Ejecutar', font=font.Font(size=13), width=10, command=execute_lexer_and_parser)
    btn_analizar.place(x=600,y=50)

    res_label = Label(root,text='',font=font.Font(size=15), width=40)
    res_label.place(x=50,y=120)

    root.mainloop()