//Learning how to take in user in put from the terminal

#include <stdio.h>
#include <string.h>

int main() {

    int age;
    char name[100];
    

    printf("Hey User! What is your name? ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("Hi %s! How old are you? ", name);
    scanf("%d", &age);
    printf("Wow %s you're %d years old! That's bonkers man.", name, age);


    return 0;
}
