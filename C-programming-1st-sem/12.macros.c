// Given the three numbers a(=8) , b(=4), c and constant value of PI =3.1415, calculate and display the following using macros (preprocessor directives).

#include <stdio.h>
// macro definition

#define PI 3.1415
#define mult(a, b) a *b
#define sum(a, b) a + b
#define sub(a, b) a - b

int main()
{
    int a = 8, b = 4;
    float mult = PI * mult(a, b);
    float sum = PI * sum(a, b);
    float sub = PI * sub(a, b);
    printf("The product is: %f", mult);
    printf("\nThe sum is: %f", sum);
    printf("\nThe subtraction is: %f", sub);
    printf("\n --[Your Name]--");

    return 0;
}
