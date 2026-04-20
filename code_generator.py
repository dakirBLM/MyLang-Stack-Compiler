import sys
sys.path.insert(0, 'generated')

from MyLangVisitor import MyLangVisitor
from MyLangParser  import MyLangParser

INT    = 'int'
FLOAT  = 'float'
BOOL   = 'bool'
STRING = 'string'
STREAM = 'stream'
TC     = {INT: 'I', FLOAT: 'F', BOOL: 'B', STRING: 'S', STREAM: 'S'}


class CodeGenerator(MyLangVisitor):
    def __init__(self, var_types):
        self.var_types    = var_types
        self.instructions = []
        self._label_ctr   = 0

    def _lbl(self):
        n = self._label_ctr
        self._label_ctr += 1
        return n

    def emit(self, i): self.instructions.append(i)
    def get_code(self): return '\n'.join(self.instructions)

    # ── pass-through wrappers ─────────────────────────────────────────────────
    def visitExprOr(self, ctx):    return self.visit(ctx.oExpr())
    def visitExprAnd(self, ctx):   return self.visit(ctx.aExpr())
    def visitExprEq(self, ctx):    return self.visit(ctx.eExpr())
    def visitExprRel(self, ctx):   return self.visit(ctx.rExpr())
    def visitExprAdd(self, ctx):   return self.visit(ctx.addE())
    def visitExprMul(self, ctx):   return self.visit(ctx.mulE())
    def visitExprUnary(self, ctx): return self.visit(ctx.unary())
    def visitExprAtom(self, ctx):  return self.visit(ctx.atom())
    def visitExprStream(self, ctx): return self.visit(ctx.streamExpr())
    def visitStreamBaseExpr(self, ctx): return self.visit(ctx.oExpr())

    # ── type inference (no emission) ──────────────────────────────────────────
    def _type(self, ctx):
        if isinstance(ctx, MyLangParser.IntLitContext):         return INT
        if isinstance(ctx, MyLangParser.FloatLitContext):       return FLOAT
        if isinstance(ctx, MyLangParser.BoolLitContext):        return BOOL
        if isinstance(ctx, MyLangParser.StringLitContext):      return STRING
        if isinstance(ctx, MyLangParser.IdExprContext):
            return self.var_types.get(ctx.ID().getText(), INT)
        if isinstance(ctx, MyLangParser.ParenExprContext):
            return self._type(ctx.expr())
        if isinstance(ctx, MyLangParser.AssignExprContext):
            return self.var_types.get(ctx.ID().getText(), INT)
        if isinstance(ctx, MyLangParser.ExprStreamContext):
            return self._type(ctx.streamExpr())
        if isinstance(ctx, MyLangParser.StreamAppendExprContext):
            return STREAM
        if isinstance(ctx, (MyLangParser.OrExprContext,  MyLangParser.AndExprContext,
                             MyLangParser.EqExprContext,  MyLangParser.RelExprContext,
                             MyLangParser.NotExprContext)):
            return BOOL
        if isinstance(ctx, MyLangParser.AddExprContext):
            op = ctx.getChild(1).getText()
            if op == '.': return STRING
            l = self._type(ctx.addE()); r = self._type(ctx.mulE())
            return FLOAT if FLOAT in (l, r) else INT
        if isinstance(ctx, MyLangParser.MulExprContext):
            op = ctx.getChild(1).getText()
            if op == '%': return INT
            l = self._type(ctx.mulE()); r = self._type(ctx.unary())
            return FLOAT if FLOAT in (l, r) else INT
        if isinstance(ctx, MyLangParser.UnaryMinusExprContext):
            return self._type(ctx.unary())
        # pass-through wrappers
        if isinstance(ctx, MyLangParser.ExprContext):    return self._type(ctx.oExpr())
        if isinstance(ctx, MyLangParser.ExprAndContext):   return self._type(ctx.aExpr())
        if isinstance(ctx, MyLangParser.ExprEqContext):    return self._type(ctx.eExpr())
        if isinstance(ctx, MyLangParser.ExprRelContext):   return self._type(ctx.rExpr())
        if isinstance(ctx, MyLangParser.ExprAddContext):   return self._type(ctx.addE())
        if isinstance(ctx, MyLangParser.ExprMulContext):   return self._type(ctx.mulE())
        if isinstance(ctx, MyLangParser.ExprUnaryContext): return self._type(ctx.unary())
        if isinstance(ctx, MyLangParser.ExprAtomContext):  return self._type(ctx.atom())
        if isinstance(ctx, MyLangParser.StreamBaseExprContext): return self._type(ctx.oExpr())
        return INT

    # ── statements ────────────────────────────────────────────────────────────
    def visitProgram(self, ctx):
        for s in ctx.statement(): self.visit(s)

    def visitEmptyStmt(self, ctx): pass

    def visitDeclStmt(self, ctx):
        typ = ctx.type_().getText()
        defaults = {INT: 'push I 0', FLOAT: 'push F 0.0',
                    BOOL: 'push B false', STRING: 'push S ""', STREAM: 'push S ""'}
        for tok in ctx.varList().ID():
            name = tok.getText()
            if typ == STREAM:
                self.emit(f'mkstream {name}')
            else:
                self.emit(defaults[typ])
                self.emit(f'save {name}')

    def visitExprStmt(self, ctx):
        self.visit(ctx.expr())
        self.emit('pop')

    def visitSaveStmt(self, ctx):
        name = ctx.ID().getText()
        self.emit(f'load {name}')
        self.emit(f'save {name}')

    def visitReadStmt(self, ctx):
        for tok in ctx.varList().ID():
            name = tok.getText()
            self.emit(f'read {TC[self.var_types[name]]}')
            self.emit(f'save {name}')

    def visitWriteStmt(self, ctx):
        exprs = ctx.exprList().expr()
        for e in exprs: self.visit(e)
        self.emit(f'print {len(exprs)}')

    def visitFWriteStmt(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.emit('fwrite')

    def visitBlockStmt(self, ctx):
        for s in ctx.statement(): self.visit(s)

    def visitIfStmt(self, ctx):
        stmts    = ctx.statement()
        has_else = len(stmts) > 1
        self.visit(ctx.expr())
        if has_else:
            el = self._lbl(); en = self._lbl()
            self.emit(f'fjmp {el}')
            self.visit(stmts[0])
            self.emit(f'jmp {en}')
            self.emit(f'label {el}')
            self.visit(stmts[1])
            self.emit(f'label {en}')
        else:
            en = self._lbl()
            self.emit(f'fjmp {en}')
            self.visit(stmts[0])
            self.emit(f'label {en}')

    def visitWhileStmt(self, ctx):
        sl = self._lbl(); el = self._lbl()
        self.emit(f'label {sl}')
        self.visit(ctx.expr())
        self.emit(f'fjmp {el}')
        self.visit(ctx.statement())
        self.emit(f'jmp {sl}')
        self.emit(f'label {el}')

    # ── literals & id ─────────────────────────────────────────────────────────
    def visitIntLit(self, ctx):
        self.emit(f'push I {ctx.getText()}'); return INT
    def visitFloatLit(self, ctx):
        self.emit(f'push F {ctx.getText()}'); return FLOAT
    def visitBoolLit(self, ctx):
        self.emit(f'push B {ctx.getText()}'); return BOOL
    def visitStringLit(self, ctx):
        self.emit(f'push S {ctx.getText()}'); return STRING
    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        self.emit(f'load {name}')
        return self.var_types.get(name, INT)
    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    # ── assignment ────────────────────────────────────────────────────────────
    def visitAssignExpr(self, ctx):
        name     = ctx.ID().getText()
        var_type = self.var_types[name]
        rhs_type = self._type(ctx.expr())
        self.visit(ctx.expr())
        if var_type == FLOAT and rhs_type == INT:
            self.emit('itof')
        self.emit(f'save {name}')
        self.emit(f'load {name}')   # assignment is an expression, returns value
        return var_type

    def visitStreamAppendExpr(self, ctx):
        name = ctx.ID().getText()
        self.visit(ctx.streamExpr())
        self.emit(f'save {name}')
        self.emit(f'load {name}')
        return STREAM

    # ── numeric binary helper ─────────────────────────────────────────────────
    def _num_bin(self, l_ctx, r_ctx, instr):
        l = self._type(l_ctx); r = self._type(r_ctx)
        res = FLOAT if FLOAT in (l, r) else INT
        self.visit(l_ctx)
        if res == FLOAT and l == INT: self.emit('itof')
        self.visit(r_ctx)
        if res == FLOAT and r == INT: self.emit('itof')
        self.emit(f'{instr} {TC[res]}')
        return res

    # ── arithmetic ────────────────────────────────────────────────────────────
    def visitAddExpr(self, ctx):
        op = ctx.getChild(1).getText()
        if op == '.':
            self.visit(ctx.addE()); self.visit(ctx.mulE())
            self.emit('concat'); return STRING
        return self._num_bin(ctx.addE(), ctx.mulE(),
                             'add' if op == '+' else 'sub')

    def visitMulExpr(self, ctx):
        op = ctx.getChild(1).getText()
        if op == '%':
            self.visit(ctx.mulE()); self.visit(ctx.unary())
            self.emit('mod'); return INT
        return self._num_bin(ctx.mulE(), ctx.unary(),
                             'mul' if op == '*' else 'div')

    def visitUnaryMinusExpr(self, ctx):
        t = self._type(ctx.unary())
        self.visit(ctx.unary())
        self.emit(f'uminus {TC[t]}')
        return t

    # ── relational (< > <= >=) ────────────────────────────────────────────────
    def visitRelExpr(self, ctx):
        op   = ctx.getChild(1).getText()
        l    = self._type(ctx.rExpr())
        r    = self._type(ctx.addE())
        base = FLOAT if FLOAT in (l, r) else INT
        # For <= : emit gt then not.  For >= : emit lt then not.
        # Normalise: <=  ->  not (>)    >=  ->  not (<)
        flip = op in ('<=', '>=')
        base_op = {'<': 'lt', '>': 'gt', '<=': 'gt', '>=': 'lt'}[op]
        self.visit(ctx.rExpr())
        if base == FLOAT and l == INT: self.emit('itof')
        self.visit(ctx.addE())
        if base == FLOAT and r == INT: self.emit('itof')
        self.emit(f'{base_op} {TC[base]}')
        if flip: self.emit('not')
        return BOOL

    # ── equality ──────────────────────────────────────────────────────────────
    def visitEqExpr(self, ctx):
        op   = ctx.getChild(1).getText()
        l    = self._type(ctx.eExpr())
        r    = self._type(ctx.rExpr())
        base = FLOAT if FLOAT in (l, r) else l
        self.visit(ctx.eExpr())
        if base == FLOAT and l == INT: self.emit('itof')
        self.visit(ctx.rExpr())
        if base == FLOAT and r == INT: self.emit('itof')
        self.emit(f'eq {TC[base]}')
        if op == '!=': self.emit('not')
        return BOOL

    # ── boolean ───────────────────────────────────────────────────────────────
    def visitOrExpr(self, ctx):
        self.visit(ctx.oExpr()); self.visit(ctx.aExpr())
        self.emit('or'); return BOOL

    def visitAndExpr(self, ctx):
        self.visit(ctx.aExpr()); self.visit(ctx.eExpr())
        self.emit('and'); return BOOL

    def visitNotExpr(self, ctx):
        self.visit(ctx.unary()); self.emit('not'); return BOOL
