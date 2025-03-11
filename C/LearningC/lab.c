#include <stdio.h>

void table(int rows, int columns, int bits, int operation)
{   
    int v;
    for (int i = 0; i <= rows; ++i){
        for (int j = 0; j <= columns; ++j){
            switch (operation)
            {
            case 0:
                v = i * j;
                break;
            case 1:
                v = i & j;
                break;
            case 2:
                v = i | j;
                break;
            }
            for(int b = 7; i >= 0; --i)
            {
                if(v & (1 << b))  // For example 0001 << 2 = 0100
                {
                    printf("1");
                }
                else
                {
                    printf("0");   
                }      
            }
            printf(" ");
        }

        printf("\n");

    }


}

int main()
{

    table(8, 8, 3, 0);
    printf("\n");
    table(8, 8, 3, 1);
    printf("\n");
    table(8, 8, 3, 2);

    return 0;
}