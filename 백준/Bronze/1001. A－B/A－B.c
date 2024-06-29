#include <stdio.h>
int main(void)
{
    int A, B;
    int min;

    scanf("%d", &A);
    scanf("%d", &B);
    
    min = A - B;
    printf("%d", min);
    
    return 0;
}