#========================================================================================#
# 					Compiler Design Project : Different operations in a compiler		 #
#																						 #
#		Team :	Aashar C K 																 #		
#				Jithin Mathew															 #
#				Megha Mariam Baby														 #
#				Minhaj Ali K															 #
#				Sreelakshmi M S															 #
#																						 #
#========================================================================================#
from ply import ctokens as tokens
from ply import lex as lex
from ply import yacc as yacc

tokens = [
    
    'NUMBER',
    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    # Increment/decrement (++,--)
    'INCREMENT', 'DECREMENT',
    # Delimeters ( ) 
    'LPAREN', 'RPAREN',
    
]
    
# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'%'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LSHIFT           = r'<<'
t_RSHIFT           = r'>>'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'

# Increment/decrement
t_INCREMENT        = r'\+\+'
t_DECREMENT        = r'--'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'

# Comment (C-Style)
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_error( t ):
  #print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIVIDE' ),
    ( 'nonassoc', 'UMINUS' )
)

# Addition

def p_add( p ) :
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]

# Substraction

def p_sub( p ) :
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]

# conversion of positive to negative

def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    p[0] = - p[2]

# Multiplication and Division

def p_mult_div( p ) :
    '''expr : expr TIMES expr
            | expr DIVIDE expr'''

    if p[2] == '*' :
  	      p[0] = p[1] * p[3]
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]

# Modulus

def p_modulus( p ) :
	'expr : expr MODULO expr'
	p[0] = p[1] % p[3]

# Bitwise Operations

# OR
def p_or( p ) :
	'expr : expr OR expr'
	p[0] = p[1] | p[3]

# AND
def p_and( p ) :
	'expr : expr AND expr'
	p[0] = p[1] & p[3]

# NOT
def p_not( p ) :
	'expr : NOT expr'
	p[0] = ~ p[2]

# XOR
def p_xor( p ) :
	'expr : expr XOR expr'
	p[0] = p[1] ^ p[3]

# R Shift
def p_rshift( p ) :
	'expr : expr RSHIFT expr'
	p[0] = p[1] >> p[3]

# L Shift
def p_lshift( p ) :
	'expr : expr LSHIFT expr'
	p[0] = p[1] << p[3]

# Logical Operators

# OR
def p_lor( p ) :
	'expr : expr LOR expr'
	p[0] = p[1] or p[3]

# AND
def p_land( p ) :
	'expr : expr LAND expr'
	p[0] = p[1] and p[3]

# NOT
def p_lnot( p ) :
	'expr : LNOT expr'
	p[0] = not p[2]

# Increment
def p_inc( p ) :
	'expr : INCREMENT expr'
	p[0] = ++ p[2]

# Decrement
def p_dec( p ) :
	'expr : DECREMENT expr'
	p[0] = -- p[2]

########################

def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]

def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

fname = "fname.c"
with open(fname) as f :
    val = f.read()
res = parser.parse(val)

print(res)
