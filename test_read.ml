// Test read, int->float promotion, modulo
int a, b, r;
float x;
string msg;

read a, b;
r = a % b;
x = a + 0.5;

write "a=", a;
write "b=", b;
write "a%b=", r;
write "a+0.5=", x;

if (r == 0) {
    write "divisible";
} else {
    write "not divisible";
}
