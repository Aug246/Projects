//Learning how to take in user in put from the terminal

#include <stdio.h>

int main() {

    int age;
    char name;

    printf("Hey User! What is your name? ");
    scanf("%c", &name);
    printf("\nHi %c! How old are you? ", name);
    scanf("%d", &age);
    printf("Wow %c you're %d years old! That's bonkers man.", name, age);


    return 0;
}
