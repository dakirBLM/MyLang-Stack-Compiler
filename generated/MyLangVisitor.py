# Generated from MyLang.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#EmptyStmt.
    def visitEmptyStmt(self, ctx:MyLangParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#DeclStmt.
    def visitDeclStmt(self, ctx:MyLangParser.DeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprStmt.
    def visitExprStmt(self, ctx:MyLangParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#SaveStmt.
    def visitSaveStmt(self, ctx:MyLangParser.SaveStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ReadStmt.
    def visitReadStmt(self, ctx:MyLangParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#WriteStmt.
    def visitWriteStmt(self, ctx:MyLangParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#FWriteStmt.
    def visitFWriteStmt(self, ctx:MyLangParser.FWriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#BlockStmt.
    def visitBlockStmt(self, ctx:MyLangParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#IfStmt.
    def visitIfStmt(self, ctx:MyLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#WhileStmt.
    def visitWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#type.
    def visitType(self, ctx:MyLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#varList.
    def visitVarList(self, ctx:MyLangParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#exprList.
    def visitExprList(self, ctx:MyLangParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AssignExpr.
    def visitAssignExpr(self, ctx:MyLangParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprStream.
    def visitExprStream(self, ctx:MyLangParser.ExprStreamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#StreamAppendExpr.
    def visitStreamAppendExpr(self, ctx:MyLangParser.StreamAppendExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#StreamBaseExpr.
    def visitStreamBaseExpr(self, ctx:MyLangParser.StreamBaseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprAnd.
    def visitExprAnd(self, ctx:MyLangParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#OrExpr.
    def visitOrExpr(self, ctx:MyLangParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AndExpr.
    def visitAndExpr(self, ctx:MyLangParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprEq.
    def visitExprEq(self, ctx:MyLangParser.ExprEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprRel.
    def visitExprRel(self, ctx:MyLangParser.ExprRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#EqExpr.
    def visitEqExpr(self, ctx:MyLangParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#RelExpr.
    def visitRelExpr(self, ctx:MyLangParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprAdd.
    def visitExprAdd(self, ctx:MyLangParser.ExprAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AddExpr.
    def visitAddExpr(self, ctx:MyLangParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprMul.
    def visitExprMul(self, ctx:MyLangParser.ExprMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#MulExpr.
    def visitMulExpr(self, ctx:MyLangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprUnary.
    def visitExprUnary(self, ctx:MyLangParser.ExprUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#NotExpr.
    def visitNotExpr(self, ctx:MyLangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MyLangParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprAtom.
    def visitExprAtom(self, ctx:MyLangParser.ExprAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ParenExpr.
    def visitParenExpr(self, ctx:MyLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#IntLit.
    def visitIntLit(self, ctx:MyLangParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#FloatLit.
    def visitFloatLit(self, ctx:MyLangParser.FloatLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#BoolLit.
    def visitBoolLit(self, ctx:MyLangParser.BoolLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#StringLit.
    def visitStringLit(self, ctx:MyLangParser.StringLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#IdExpr.
    def visitIdExpr(self, ctx:MyLangParser.IdExprContext):
        return self.visitChildren(ctx)



del MyLangParser