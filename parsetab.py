
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEnonassocUMINUSNUMBER PLUS MINUS TIMES DIVIDE MODULO OR AND NOT XOR LSHIFT RSHIFT LOR LAND LNOT INCREMENT DECREMENT LPAREN RPARENexpr : expr PLUS exprexpr : expr MINUS exprexpr : MINUS expr %prec UMINUSexpr : expr TIMES expr\n            | expr DIVIDE exprexpr : expr MODULO exprexpr : expr OR exprexpr : expr AND exprexpr : NOT exprexpr : expr XOR exprexpr : expr RSHIFT exprexpr : expr LSHIFT exprexpr : expr LOR exprexpr : expr LAND exprexpr : LNOT exprexpr : INCREMENT exprexpr : DECREMENT exprexpr : NUMBERexpr : LPAREN expr RPAREN'
    
_lr_action_items = {'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[2,10,2,2,2,2,2,-18,2,2,2,2,2,2,2,2,2,2,2,2,2,-3,10,10,10,10,10,-1,-2,-4,-5,10,10,10,10,10,10,10,10,-19,]),'NOT':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'LNOT':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'INCREMENT':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'DECREMENT':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'NUMBER':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'LPAREN':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,7,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,],[0,-18,-3,-9,-15,-16,-17,-1,-2,-4,-5,-6,-7,-8,-10,-11,-12,-13,-14,-19,]),'PLUS':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[9,-18,-3,9,9,9,9,9,-1,-2,-4,-5,9,9,9,9,9,9,9,9,-19,]),'TIMES':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[11,-18,-3,11,11,11,11,11,11,11,-4,-5,11,11,11,11,11,11,11,11,-19,]),'DIVIDE':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[12,-18,-3,12,12,12,12,12,12,12,-4,-5,12,12,12,12,12,12,12,12,-19,]),'MODULO':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[13,-18,-3,13,13,13,13,13,-1,-2,-4,-5,13,13,13,13,13,13,13,13,-19,]),'OR':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[14,-18,-3,14,14,14,14,14,-1,-2,-4,-5,14,14,14,14,14,14,14,14,-19,]),'AND':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[15,-18,-3,15,15,15,15,15,-1,-2,-4,-5,15,15,15,15,15,15,15,15,-19,]),'XOR':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[16,-18,-3,16,16,16,16,16,-1,-2,-4,-5,16,16,16,16,16,16,16,16,-19,]),'RSHIFT':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[17,-18,-3,17,17,17,17,17,-1,-2,-4,-5,17,17,17,17,17,17,17,17,-19,]),'LSHIFT':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[18,-18,-3,18,18,18,18,18,-1,-2,-4,-5,18,18,18,18,18,18,18,18,-19,]),'LOR':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[19,-18,-3,19,19,19,19,19,-1,-2,-4,-5,19,19,19,19,19,19,19,19,-19,]),'LAND':([1,7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[20,-18,-3,20,20,20,20,20,-1,-2,-4,-5,20,20,20,20,20,20,20,20,-19,]),'RPAREN':([7,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[-18,-3,-9,-15,-16,-17,39,-1,-2,-4,-5,-6,-7,-8,-10,-11,-12,-13,-14,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,],[1,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr PLUS expr','expr',3,'p_add','compiler.py',83),
  ('expr -> expr MINUS expr','expr',3,'p_sub','compiler.py',89),
  ('expr -> MINUS expr','expr',2,'p_expr2uminus','compiler.py',95),
  ('expr -> expr TIMES expr','expr',3,'p_mult_div','compiler.py',101),
  ('expr -> expr DIVIDE expr','expr',3,'p_mult_div','compiler.py',102),
  ('expr -> expr MODULO expr','expr',3,'p_modulus','compiler.py',115),
  ('expr -> expr OR expr','expr',3,'p_or','compiler.py',122),
  ('expr -> expr AND expr','expr',3,'p_and','compiler.py',127),
  ('expr -> NOT expr','expr',2,'p_not','compiler.py',132),
  ('expr -> expr XOR expr','expr',3,'p_xor','compiler.py',137),
  ('expr -> expr RSHIFT expr','expr',3,'p_rshift','compiler.py',142),
  ('expr -> expr LSHIFT expr','expr',3,'p_lshift','compiler.py',147),
  ('expr -> expr LOR expr','expr',3,'p_lor','compiler.py',154),
  ('expr -> expr LAND expr','expr',3,'p_land','compiler.py',159),
  ('expr -> LNOT expr','expr',2,'p_lnot','compiler.py',164),
  ('expr -> INCREMENT expr','expr',2,'p_inc','compiler.py',169),
  ('expr -> DECREMENT expr','expr',2,'p_dec','compiler.py',174),
  ('expr -> NUMBER','expr',1,'p_expr2NUM','compiler.py',180),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_parens','compiler.py',184),
]
