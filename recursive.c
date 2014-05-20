/* C version. */
#include <stdio.h>
#include <stdlib.h>

int calculate(int acc, int times) {
    if(times == 0) return acc;

    int n = 0;
    if(scanf("%d", &n) != 1) exit(-1);
    return calculate(acc + (n>0? n*n: 0), times - 1);
}

void sub_question(int times) {
    int n = 0;
    if(scanf("%d", &n) != 1) exit(-1);
    printf("%d\n", calculate(0, n));

    if(times > 1) {
        sub_question(times - 1);
    }
}

int main() {
    int times;
    if(scanf("%d", &times) != 1) exit(-1);
    sub_question(times);
    return 0;
}
