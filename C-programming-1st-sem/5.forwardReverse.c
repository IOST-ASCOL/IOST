/*Write a program to prompt the user to input 3 integer values and print these values in forward and reversed order.
 */

#include <stdio.h>

int main()
{
    int num1, num2, num3;
    printf("Enter any 3 integers: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    printf("\nThe integers in forward order: %d %d %d", num1, num2, num3);
    printf("\nThe integers in reversed order: %d %d %d", num3, num2, num1);
    printf("\n --[Your name]--");

    return 0;
}