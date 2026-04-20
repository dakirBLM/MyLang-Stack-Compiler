// Error sample: type errors
int x;
float y;
bool flag;

x = 3.14;         // error: float assigned to int
y = x + flag;     // error: adding int and bool
x = x + x;       // ok
int x;            // error: redeclared
