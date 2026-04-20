grammar MyLang;

// ─── Parser Rules ───────────────────────────────────────────────────────────

program : statement* EOF ;

statement
    : ';'                                          # EmptyStmt
    | type varList ';'                             # DeclStmt
    | expr ';'                                     # ExprStmt
    | READ varList ';'                             # ReadStmt
    | WRITE exprList ';'                           # WriteStmt
    | FWRITE expr expr ';'                         # FWriteStmt
    | '{' statement* '}'                           # BlockStmt
    | IF '(' expr ')' statement (ELSE statement)?  # IfStmt
    | WHILE '(' expr ')' statement                 # WhileStmt
    ;

type : INT_TYPE | FLOAT_TYPE | BOOL_TYPE | STRING_TYPE | STREAM ;

varList  : ID (',' ID)* ;
exprList : expr (',' expr)* ;

// Assignment: right-assoc, lowest priority, LHS must be a plain ID
expr
    : ID '=' expr                                  # AssignExpr
    | streamExpr                                   # ExprStream
    ;

streamExpr
    : ID '<<' streamExpr                           # StreamAppendExpr
    | oExpr                                        # StreamBaseExpr
    ;

oExpr
    : oExpr '||' aExpr                             # OrExpr
    | aExpr                                        # ExprAnd
    ;

aExpr
    : aExpr '&&' eExpr                             # AndExpr
    | eExpr                                        # ExprEq
    ;

eExpr
    : eExpr ('==' | '!=') rExpr                    # EqExpr
    | rExpr                                        # ExprRel
    ;

rExpr
    : rExpr ('<' | '>' | '<=' | '>=') addE         # RelExpr
    | addE                                         # ExprAdd
    ;

addE
    : addE ('+' | '-' | '.') mulE                  # AddExpr
    | mulE                                         # ExprMul
    ;

mulE
    : mulE ('*' | '/' | '%') unary                 # MulExpr
    | unary                                        # ExprUnary
    ;

unary
    : '!' unary                                    # NotExpr
    | '-' unary                                    # UnaryMinusExpr
    | atom                                         # ExprAtom
    ;

atom
    : '(' expr ')'                                 # ParenExpr
    | INT_LIT                                      # IntLit
    | FLOAT_LIT                                    # FloatLit
    | BOOL_LIT                                     # BoolLit
    | STRING_LIT                                   # StringLit
    | ID                                           # IdExpr
    ;





// ─── Lexer Rules ─────────────────────────────────────────────────────────────

INT_TYPE    : 'int' ;
FLOAT_TYPE  : 'float' ;
BOOL_TYPE   : 'bool' ;
STRING_TYPE : 'string' ;
STREAM      : 'stream' ;
IF          : 'if' ;
ELSE        : 'else' ;
WHILE       : 'while' ;
READ        : 'read' ;
WRITE       : 'write' ;
FWRITE      : 'fwrite' ;
BOOL_LIT    : 'true' | 'false' ;

FLOAT_LIT  : [0-9]+ '.' [0-9]* | [0-9]* '.' [0-9]+ ;
INT_LIT    : [0-9]+ ;
STRING_LIT : '"' (~["\r\n\\] | '\\' .)* '"' ;
ID         : [a-zA-Z][a-zA-Z0-9]* ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WS           : [ \t\r\n]+   -> skip ;
