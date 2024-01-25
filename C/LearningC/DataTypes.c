//Code exploring and learning various data types
/*
int | %d - interger values(whole numbers)
double | %lf - can hold decimal values to a higher precision
float | %f - same as double but less decimal places
char | %c
sizeof(variable) | %zu - prints the size of the variable
*/

#include <stdio.h>

int main(){

    int age = 10;
    printf("Age is %d\n\n", age);

    double number = 12.45;
    printf("Your number is %.2lf\n\n", number);

    float secondNumber = 13.91f;
    printf("Your second number is %.2f\n\n", secondNumber);

    char nameInitial = 'A';
    printf("My initial is %c\n\n", nameInitial);

    printf("Age size = %zu\n", sizeof(age));
    printf("Number size = %zu\n", sizeof(number));
    printf("Second number size = %zu\n", sizeof(secondNumber));
    printf("Initial size = %zu", sizeof(nameInitial));

    return 0;
}