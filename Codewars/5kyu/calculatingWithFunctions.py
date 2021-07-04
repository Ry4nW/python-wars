import operator
ops = { "+ ": operator.add, "- ": operator.sub, "//": operator.floordiv, "* ": operator.mul}

def zero(op=None): return ops[op[0:2]](0, int(op[2])) if op != None else 0
def one(op=None): return ops[op[0:2]](1, int(op[2])) if op != None else 1
def two(op=None): return ops[op[0:2]](2, int(op[2])) if op != None else 2
def three(op=None): return ops[op[0:2]](3, int(op[2])) if op != None else 3
def four(op=None): return ops[op[0:2]](4, int(op[2])) if op != None else 4
def five(op=None): return ops[op[0:2]](5, int(op[2])) if op != None else 5
def six(op=None): return ops[op[0:2]](6, int(op[2])) if op != None else 6
def seven(op=None): return ops[op[0:2]](7, int(op[2])) if op != None else 7
def eight(op=None): return ops[op[0:2]](8, int(op[2])) if op != None else 8
def nine(op=None): return ops[op[0:2]](9, int(op[2])) if op != None else 9

def plus(num): return '+ ' + str(num) 
def minus(num): return '- ' + str(num) 
def times(num): return '* ' + str(num) 
def divided_by(num): return '//' + str(num) 