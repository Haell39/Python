#include <stdio.h>

int main() {
    int x = 0, y, z;


    printf("Enter a number to set a list of numbers: ");
    scanf("%d", &y);

    while (x <= y) {
        printf("choose a number from 0 to %d, press 0 to exit ", y);
        scanf("%d", &z);
        if(z == 0) {
            printf("exiting programing");
            break;
        }  if (z % 2 == 0) {
            printf("%d is even\n", z);
        } else {
            printf("%d is odd\n", z);
        }
        x = x + 1;
    }



    return 0;
}