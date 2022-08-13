
import re

import ply.lex as lex

reservadas = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'CALL', 'CONST',
              'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE'
              ]

tokens = list(reservadas+['IDENTIFICADOR', 'NUMERO', 'SUMA', 'RESTA', 'MULTIPLICACION',
                          'DIVISION',
                          'PAR', 'ASIGNACION', 'DIFERENTE', 'MENOR', 'MENORQUE',
                          'MAYOR', 'MAYORQUE',
                          'IPARENTESIS', 'DPARENTESIS', 'COMA', 'PUNTOCOMA',
                          'PUNTO', 'IGUAL'
                          ])

t_ignore = '\t '
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PAR = r'PAR'
t_ASIGNACION = r'='
t_DIFERENTE = r'<>'
t_MENOR = r'<'
t_MENORQUE = r'<='
t_MAYOR = r'>'
t_MAYORQUE = r'>='
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'
t_COMA = r','
t_PUNTOCOMA = r';'
t_PUNTO = r'\.'
t_IGUAL = r':='


def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value

    return t


def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMENTARIO(t):
    r'\#.*'
    pass


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    t.lexer.skip(1)
    return "Caracter Ilegal"


def analizador(cadena):
    resultado_analizador = []
    analizador = lex.lex()
    print(analizador)
    analizador.input(cadena)
    while True:
        tok = analizador.token()
        print(tok)
        if not tok:
            break
        resultado_analizador.append("Número línea: "+str(tok.lineno) + " "+str(tok.type) +
                                    " "+str(tok.value)
                                    )
    return resultado_analizador
