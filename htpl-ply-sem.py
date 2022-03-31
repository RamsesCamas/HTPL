import ply.lex as lex
import ply.yacc as yacc
import re
import regex

ERROR = False
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
t_INPUTVAR = r'(?<=assign=").*(?="\s)'
t_CONTENT = r'(?<=>).*(?=<)'
t_INPUT= r'input'
t_ASSIGN = r'assign'
t_PRINT = r'print'
t_DOLLAR = r'\$'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LANGNAME = r'HTPL'

variables = dict({})

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
    pass

def p_input(p):
    #<input assign=“hola” type="string">
    'expresion : LARROW INPUT ASSIGN EQUAL QUOTE INPUTVAR QUOTE TYPE EQUAL QUOTE DATATYPE QUOTE RARROW'
    pass

def p_print(p):
    'expresion : LARROW PRINT RARROW CONTENT LARROW SLASH PRINT RARROW'
    pass

def p_print_v(p):
    'expresion : LARROW PRINT RARROW print-v LARROW SLASH PRINT RARROW'
    pass

def p_print_var(p):
    'print-v : DOLLAR LBRACE IDENT RBRACE'
    pass

def p_error(p):
    error = 'Token(s) inválidos'
    if p is not None:
        error = f"Error de sintáxis en el carácter número: {p.lexpos+1}."
    global ERROR
    print(error)
    ERROR = True

def read_variable(entry):
    global ERROR
    var_type = regex.findall(r'(?<=type=").*(?="\s)',entry)[0]
    var_type = var_type.replace(' ','')
    var_name = regex.findall(r'(?<=name=").*(?="[\s]*)',entry)[0]
    var_name = var_name.replace(' ','')
    var_value = regex.findall(r'(?<=">\s).*(?=\s</var>)',entry)[0]
    if var_value[0] == ' ':
        var_value = var_value[1:]
    if var_type == 'integer':
        try:
            var_value = int(var_value)
        except:
            print('Error de tipo: No se puede convertir a Entero')
            ERROR = True
    elif var_type == 'float':
        try:
            var_value = float(var_value)
        except:
            print('Error de tipo: No se puede convertir a flotante')
            ERROR = True
    elif var_type == 'boolean':
        try:
            if var_value == 'False':
                var_value = False
            elif var_value == 'True':
                var_value = True
            else:
                raise Exception()
        except:
            print('No se puede declarar tipo booleano')
            ERROR = True
    if not ERROR:
        variables[f'{var_name}'] = {'tipo':var_type,'valor':var_value}

def read_input(entry):
    #<input assign="my_input" type="string">
    global ERROR
    var_name = regex.findall(r'(?<=assign=").*(?="\s)',entry)[0]
    var_name = var_name.replace(' ','')
    var_type = regex.findall(r'(?<=type=").*(?=")',entry)[0]
    var_type = var_type.replace(' ','')
    var_value = input('Ingrese el valor: ')
    if var_type == 'integer':
        try:
            var_value = int(var_value)
        except:
            print('Error de tipo: No se puede convertir a Entero')
            ERROR = True
    elif var_type == 'float':
        try:
            var_value = float(var_value)
        except:
            print('Error de tipo: No se puede convertir a flotante')
            ERROR = True
    elif var_type == 'boolean':
        try:
            if var_value == 'False':
                var_value = False
            elif var_value == 'True':
                var_value = True
            else:
                raise Exception()
        except:
            print('No se puede declarar tipo booleano')
            ERROR = True
    if not ERROR:
        variables[f'{var_name}'] = {'tipo':var_type,'valor':var_value}

def print_things(entry):
    #<print> Me llamo ${my_string} y tengo ${my_int} años. </print>
    #<print> ¿Cómo te llamas? </print>
    global ERROR
    sentence = regex.findall(r'(?<=<print>).*(?=</print>)',entry)[0]
    sentence = sentence.split(' ')
    while '' in sentence:
        sentence.remove('')
    sentence = ' '.join(sentence)
    vars_to_print = regex.findall(r'(?<=\$\{)\w+(?=\})',sentence)
    for variable in vars_to_print:
        temp_var = variables.get(variable).get('valor')
        variable = '${' + variable + '}'
        sentence = sentence.replace(variable,str(temp_var))
    print(sentence)
parser = yacc.yacc()

def execute_lexer_and_parser(entrada):
    formated_entry = re.sub('> +(?=[\w]*)','>',entrada)
    global ERROR
    ERROR = False
    parser.parse(formated_entry)
    lexer.input(formated_entry)


if __name__=='__main__':
    while (source := input('>> ')) != 'exit()':
        execute_lexer_and_parser(source)
        if not ERROR:
            if '</var>' in source:
                read_variable(source)
            elif '<input' in source:
                read_input(source)
            elif '<print>' in source:
                print_things(source)
