#include <stdio.h>

int main(){

    int b = 582;
    int a = 0;
    int max = ((a << 2) | (b <<4) | (a & b)) & 0xF351;
    for (a = 1; a <= 99; ++a){
        int num = ((a << 2) | (b <<4) | (a & b)) & 0xF351;
        if (num > max)
            num = max;
    }
    printf("%d", max);
    return 0;
}