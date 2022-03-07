
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CONTENT DATATYPE DOLLAR EQUAL IDENT INPUT INPUTVAR LANGNAME LARROW LBRACE NAME PRINT QUOTE RARROW RBRACE SLASH TYPE VARentrada : expresionexpresion : LARROW VAR TYPE EQUAL QUOTE DATATYPE QUOTE NAME EQUAL QUOTE IDENT QUOTE RARROW CONTENT LARROW SLASH VAR RARROWexpresion : LARROW INPUT ASSIGN EQUAL QUOTE INPUTVAR QUOTE RARROWexpresion : LARROW PRINT RARROW CONTENT LARROW SLASH PRINT RARROWexpresion : LARROW PRINT RARROW print-v LARROW SLASH PRINT RARROWprint-v : DOLLAR LBRACE IDENT RBRACE'
    
_lr_action_items = {'LARROW':([0,12,13,29,39,],[3,17,18,-6,40,]),'$end':([1,2,31,32,33,43,],[0,-1,-3,-4,-5,-2,]),'VAR':([3,41,],[4,42,]),'INPUT':([3,],[5,]),'PRINT':([3,22,23,],[6,27,28,]),'TYPE':([4,],[7,]),'ASSIGN':([5,],[8,]),'RARROW':([6,26,27,28,37,42,],[9,31,32,33,38,43,]),'EQUAL':([7,8,30,],[10,11,34,]),'CONTENT':([9,38,],[12,39,]),'DOLLAR':([9,],[14,]),'QUOTE':([10,11,20,21,34,36,],[15,16,25,26,35,37,]),'LBRACE':([14,],[19,]),'DATATYPE':([15,],[20,]),'INPUTVAR':([16,],[21,]),'SLASH':([17,18,40,],[22,23,41,]),'IDENT':([19,35,],[24,36,]),'RBRACE':([24,],[29,]),'NAME':([25,],[30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'entrada':([0,],[1,]),'expresion':([0,],[2,]),'print-v':([9,],[13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> entrada","S'",1,None,None,None),
  ('entrada -> expresion','entrada',1,'p_start','htpl-ply.py',67),
  ('expresion -> LARROW VAR TYPE EQUAL QUOTE DATATYPE QUOTE NAME EQUAL QUOTE IDENT QUOTE RARROW CONTENT LARROW SLASH VAR RARROW','expresion',18,'p_variable','htpl-ply.py',70),
  ('expresion -> LARROW INPUT ASSIGN EQUAL QUOTE INPUTVAR QUOTE RARROW','expresion',8,'p_input','htpl-ply.py',75),
  ('expresion -> LARROW PRINT RARROW CONTENT LARROW SLASH PRINT RARROW','expresion',8,'p_print','htpl-ply.py',81),
  ('expresion -> LARROW PRINT RARROW print-v LARROW SLASH PRINT RARROW','expresion',8,'p_print_v','htpl-ply.py',86),
  ('print-v -> DOLLAR LBRACE IDENT RBRACE','print-v',4,'p_print_var','htpl-ply.py',91),
]
