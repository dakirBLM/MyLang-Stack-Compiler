// Test: FizzBuzz
int i;
i = 1;
while (i <= 20) {
    if (i % 15 == 0) {
        write "FizzBuzz";
    } else {
        if (i % 3 == 0) {
            write "Fizz";
        } else {
            if (i % 5 == 0) {
                write "Buzz";
            } else {
                write i;
            }
        }
    }
    i = i + 1;
}
