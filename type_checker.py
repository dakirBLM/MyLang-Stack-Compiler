import sys
sys.path.insert(0, 'generated')

from MyLangVisitor import MyLangVisitor
from MyLangParser  import MyLangParser

INT    = 'int'
FLOAT  = 'float'
BOOL   = 'bool'
STRING = 'string'
STREAM = 'stream'


class TypeChecker(MyLangVisitor):
    def __init__(self):
        self.variables = {}   # name -> type
        self.errors    = []

    def _err(self, ctx, msg):
        line = ctx.start.line if hasattr(ctx, 'start') else '?'
        self.errors.append(f"Type error at line {line}: {msg}")

    def _promote(self, l, r):
        if (l == INT and r == FLOAT) or (l == FLOAT and r == INT):
            return FLOAT, FLOAT
        return l, r

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

    def visitStreamAppendExpr(self, ctx):
        name = ctx.ID().getText()
        var_type = self.variables.get(name)
        if var_type is None:
            self._err(ctx, f"Variable '{name}' not declared.")
        elif var_type != STREAM:
            self._err(ctx, f"'<<' requires a stream on the left, got '{var_type}'.")
        self.visit(ctx.streamExpr())
        return STREAM

    # ── statements ────────────────────────────────────────────────────────────
    def visitProgram(self, ctx):
        for s in ctx.statement(): self.visit(s)

    def visitEmptyStmt(self, ctx): pass

    def visitDeclStmt(self, ctx):
        typ = self.visit(ctx.type_())
        for tok in ctx.varList().ID():
            name = tok.getText()
            if name in self.variables:
                self.errors.append(
                    f"Type error at line {tok.symbol.line}: "
                    f"Variable '{name}' already declared.")
            else:
                self.variables[name] = typ

    def visitExprStmt(self, ctx): self.visit(ctx.expr())

    def visitSaveStmt(self, ctx):
        name = ctx.ID().getText()
        var_type = self.variables.get(name)
        if var_type is None:
            self._err(ctx, f"Variable '{name}' not declared.")
            return
        if var_type != STREAM:
            self._err(ctx, f"'save' statement is only valid for stream variables, got '{var_type}'.")

    def visitReadStmt(self, ctx):
        for tok in ctx.varList().ID():
            name = tok.getText()
            if name not in self.variables:
                self.errors.append(
                    f"Type error at line {tok.symbol.line}: "
                    f"Variable '{name}' not declared.")

    def visitWriteStmt(self, ctx):
        for e in ctx.exprList().expr(): self.visit(e)

    def visitFWriteStmt(self, ctx):
        stream_type = self.visit(ctx.expr(0))
        file_type = self.visit(ctx.expr(1))
        if stream_type != STREAM:
            self._err(ctx.expr(0), f"'fwrite' requires a stream as the first argument, got '{stream_type}'.")
        if file_type != STRING:
            self._err(ctx.expr(1), f"'fwrite' requires a string file name as the second argument, got '{file_type}'.")

    def visitBlockStmt(self, ctx):
        for s in ctx.statement(): self.visit(s)

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond != BOOL:
            self._err(ctx.expr(), f"'if' condition must be bool, got '{cond}'.")
        for s in ctx.statement(): self.visit(s)

    def visitWhileStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond != BOOL:
            self._err(ctx.expr(), f"'while' condition must be bool, got '{cond}'.")
        self.visit(ctx.statement())

    def visitType(self, ctx):
        return ctx.getText()

    # ── literals & id ─────────────────────────────────────────────────────────
    def visitIntLit(self, ctx):    return INT
    def visitFloatLit(self, ctx):  return FLOAT
    def visitBoolLit(self, ctx):   return BOOL
    def visitStringLit(self, ctx): return STRING

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.variables:
            self._err(ctx, f"Variable '{name}' not declared.")
            return None
        return self.variables[name]

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    # ── assignment ────────────────────────────────────────────────────────────
    def visitAssignExpr(self, ctx):
        name     = ctx.ID().getText()
        var_type = self.variables.get(name)
        if var_type is None:
            self._err(ctx, f"Variable '{name}' not declared.")
        rhs_type = self.visit(ctx.expr())
        if var_type == FLOAT and rhs_type == INT:
            rhs_type = FLOAT
        if var_type is not None and var_type != rhs_type:
            self._err(ctx,
                f"Cannot assign '{rhs_type}' to '{name}' (type '{var_type}').")
        return var_type

    # ── boolean ───────────────────────────────────────────────────────────────
    def visitOrExpr(self, ctx):
        l, r = self.visit(ctx.oExpr()), self.visit(ctx.aExpr())
        if l != BOOL or r != BOOL:
            self._err(ctx, f"'||' requires bool, got '{l}' and '{r}'.")
        return BOOL

    def visitAndExpr(self, ctx):
        l, r = self.visit(ctx.aExpr()), self.visit(ctx.eExpr())
        if l != BOOL or r != BOOL:
            self._err(ctx, f"'&&' requires bool, got '{l}' and '{r}'.")
        return BOOL

    def visitNotExpr(self, ctx):
        t = self.visit(ctx.unary())
        if t != BOOL:
            self._err(ctx, f"'!' requires bool, got '{t}'.")
        return BOOL

    def visitUnaryMinusExpr(self, ctx):
        t = self.visit(ctx.unary())
        if t not in (INT, FLOAT):
            self._err(ctx, f"Unary '-' requires int or float, got '{t}'.")
            return INT
        return t

    # ── equality / relational ─────────────────────────────────────────────────
    def visitEqExpr(self, ctx):
        op   = ctx.getChild(1).getText()
        l, r = self.visit(ctx.eExpr()), self.visit(ctx.rExpr())
        l, r = self._promote(l, r)
        if l != r:
            self._err(ctx, f"'{op}' needs same type on both sides, got '{l}' and '{r}'.")
        elif l not in (INT, FLOAT, STRING, STREAM):
            self._err(ctx, f"'{op}' not defined for type '{l}'.")
        return BOOL

    def visitRelExpr(self, ctx):
        op   = ctx.getChild(1).getText()
        l, r = self.visit(ctx.rExpr()), self.visit(ctx.addE())
        l, r = self._promote(l, r)
        if l != r or l not in (INT, FLOAT):
            self._err(ctx, f"'{op}' requires int or float, got '{l}' and '{r}'.")
        return BOOL

    # ── arithmetic ────────────────────────────────────────────────────────────
    def visitAddExpr(self, ctx):
        op   = ctx.getChild(1).getText()
        l, r = self.visit(ctx.addE()), self.visit(ctx.mulE())
        if op == '.':
            if l != STRING or r != STRING:
                self._err(ctx, f"'.' requires string operands, got '{l}' and '{r}'.")
            return STRING
        l, r = self._promote(l, r)
        if l != r or l not in (INT, FLOAT):
            self._err(ctx, f"'{op}' requires int or float, got '{l}' and '{r}'.")
            return INT
        return l


    def visitMulExpr(self, ctx):
        op   = ctx.getChild(1).getText()
        l, r = self.visit(ctx.mulE()), self.visit(ctx.unary())
        if op == '%':
            if l != INT or r != INT:
                self._err(ctx, f"'%' requires int operands, got '{l}' and '{r}'.")
            return INT
        l, r = self._promote(l, r)
        if l != r or l not in (INT, FLOAT):
            self._err(ctx, f"'{op}' requires int or float, got '{l}' and '{r}'.")
            return INT
        return l
