# Generated from MyLang.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#EmptyStmt.
    def enterEmptyStmt(self, ctx:MyLangParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#EmptyStmt.
    def exitEmptyStmt(self, ctx:MyLangParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#DeclStmt.
    def enterDeclStmt(self, ctx:MyLangParser.DeclStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#DeclStmt.
    def exitDeclStmt(self, ctx:MyLangParser.DeclStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprStmt.
    def enterExprStmt(self, ctx:MyLangParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprStmt.
    def exitExprStmt(self, ctx:MyLangParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#SaveStmt.
    def enterSaveStmt(self, ctx:MyLangParser.SaveStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#SaveStmt.
    def exitSaveStmt(self, ctx:MyLangParser.SaveStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#ReadStmt.
    def enterReadStmt(self, ctx:MyLangParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#ReadStmt.
    def exitReadStmt(self, ctx:MyLangParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#WriteStmt.
    def enterWriteStmt(self, ctx:MyLangParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#WriteStmt.
    def exitWriteStmt(self, ctx:MyLangParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#FWriteStmt.
    def enterFWriteStmt(self, ctx:MyLangParser.FWriteStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#FWriteStmt.
    def exitFWriteStmt(self, ctx:MyLangParser.FWriteStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#BlockStmt.
    def enterBlockStmt(self, ctx:MyLangParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#BlockStmt.
    def exitBlockStmt(self, ctx:MyLangParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#IfStmt.
    def enterIfStmt(self, ctx:MyLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#IfStmt.
    def exitIfStmt(self, ctx:MyLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#WhileStmt.
    def enterWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#WhileStmt.
    def exitWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#type.
    def enterType(self, ctx:MyLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MyLangParser#type.
    def exitType(self, ctx:MyLangParser.TypeContext):
        pass


    # Enter a parse tree produced by MyLangParser#varList.
    def enterVarList(self, ctx:MyLangParser.VarListContext):
        pass

    # Exit a parse tree produced by MyLangParser#varList.
    def exitVarList(self, ctx:MyLangParser.VarListContext):
        pass


    # Enter a parse tree produced by MyLangParser#exprList.
    def enterExprList(self, ctx:MyLangParser.ExprListContext):
        pass

    # Exit a parse tree produced by MyLangParser#exprList.
    def exitExprList(self, ctx:MyLangParser.ExprListContext):
        pass


    # Enter a parse tree produced by MyLangParser#AssignExpr.
    def enterAssignExpr(self, ctx:MyLangParser.AssignExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#AssignExpr.
    def exitAssignExpr(self, ctx:MyLangParser.AssignExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprStream.
    def enterExprStream(self, ctx:MyLangParser.ExprStreamContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprStream.
    def exitExprStream(self, ctx:MyLangParser.ExprStreamContext):
        pass


    # Enter a parse tree produced by MyLangParser#StreamAppendExpr.
    def enterStreamAppendExpr(self, ctx:MyLangParser.StreamAppendExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#StreamAppendExpr.
    def exitStreamAppendExpr(self, ctx:MyLangParser.StreamAppendExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#StreamBaseExpr.
    def enterStreamBaseExpr(self, ctx:MyLangParser.StreamBaseExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#StreamBaseExpr.
    def exitStreamBaseExpr(self, ctx:MyLangParser.StreamBaseExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprAnd.
    def enterExprAnd(self, ctx:MyLangParser.ExprAndContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprAnd.
    def exitExprAnd(self, ctx:MyLangParser.ExprAndContext):
        pass


    # Enter a parse tree produced by MyLangParser#OrExpr.
    def enterOrExpr(self, ctx:MyLangParser.OrExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#OrExpr.
    def exitOrExpr(self, ctx:MyLangParser.OrExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#AndExpr.
    def enterAndExpr(self, ctx:MyLangParser.AndExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#AndExpr.
    def exitAndExpr(self, ctx:MyLangParser.AndExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprEq.
    def enterExprEq(self, ctx:MyLangParser.ExprEqContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprEq.
    def exitExprEq(self, ctx:MyLangParser.ExprEqContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprRel.
    def enterExprRel(self, ctx:MyLangParser.ExprRelContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprRel.
    def exitExprRel(self, ctx:MyLangParser.ExprRelContext):
        pass


    # Enter a parse tree produced by MyLangParser#EqExpr.
    def enterEqExpr(self, ctx:MyLangParser.EqExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#EqExpr.
    def exitEqExpr(self, ctx:MyLangParser.EqExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#RelExpr.
    def enterRelExpr(self, ctx:MyLangParser.RelExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#RelExpr.
    def exitRelExpr(self, ctx:MyLangParser.RelExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprAdd.
    def enterExprAdd(self, ctx:MyLangParser.ExprAddContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprAdd.
    def exitExprAdd(self, ctx:MyLangParser.ExprAddContext):
        pass


    # Enter a parse tree produced by MyLangParser#AddExpr.
    def enterAddExpr(self, ctx:MyLangParser.AddExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#AddExpr.
    def exitAddExpr(self, ctx:MyLangParser.AddExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprMul.
    def enterExprMul(self, ctx:MyLangParser.ExprMulContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprMul.
    def exitExprMul(self, ctx:MyLangParser.ExprMulContext):
        pass


    # Enter a parse tree produced by MyLangParser#MulExpr.
    def enterMulExpr(self, ctx:MyLangParser.MulExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#MulExpr.
    def exitMulExpr(self, ctx:MyLangParser.MulExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprUnary.
    def enterExprUnary(self, ctx:MyLangParser.ExprUnaryContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprUnary.
    def exitExprUnary(self, ctx:MyLangParser.ExprUnaryContext):
        pass


    # Enter a parse tree produced by MyLangParser#NotExpr.
    def enterNotExpr(self, ctx:MyLangParser.NotExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#NotExpr.
    def exitNotExpr(self, ctx:MyLangParser.NotExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:MyLangParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:MyLangParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprAtom.
    def enterExprAtom(self, ctx:MyLangParser.ExprAtomContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprAtom.
    def exitExprAtom(self, ctx:MyLangParser.ExprAtomContext):
        pass


    # Enter a parse tree produced by MyLangParser#ParenExpr.
    def enterParenExpr(self, ctx:MyLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#ParenExpr.
    def exitParenExpr(self, ctx:MyLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#IntLit.
    def enterIntLit(self, ctx:MyLangParser.IntLitContext):
        pass

    # Exit a parse tree produced by MyLangParser#IntLit.
    def exitIntLit(self, ctx:MyLangParser.IntLitContext):
        pass


    # Enter a parse tree produced by MyLangParser#FloatLit.
    def enterFloatLit(self, ctx:MyLangParser.FloatLitContext):
        pass

    # Exit a parse tree produced by MyLangParser#FloatLit.
    def exitFloatLit(self, ctx:MyLangParser.FloatLitContext):
        pass


    # Enter a parse tree produced by MyLangParser#BoolLit.
    def enterBoolLit(self, ctx:MyLangParser.BoolLitContext):
        pass

    # Exit a parse tree produced by MyLangParser#BoolLit.
    def exitBoolLit(self, ctx:MyLangParser.BoolLitContext):
        pass


    # Enter a parse tree produced by MyLangParser#StringLit.
    def enterStringLit(self, ctx:MyLangParser.StringLitContext):
        pass

    # Exit a parse tree produced by MyLangParser#StringLit.
    def exitStringLit(self, ctx:MyLangParser.StringLitContext):
        pass


    # Enter a parse tree produced by MyLangParser#IdExpr.
    def enterIdExpr(self, ctx:MyLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#IdExpr.
    def exitIdExpr(self, ctx:MyLangParser.IdExprContext):
        pass



del MyLangParser